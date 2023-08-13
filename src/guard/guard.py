from guard.util import Direction, to_schema_string
from guard.query_parser import extract_rel_patterns

class CypherGuard():
    # Main class for the utility. Needs to be initialized with a schema, then called using the `run()` function.
    schema_patterns: set
    schema_labels: set

    def __init__(self, schema_string) -> None:
        self.schema_labels = set()
        self.schema_patterns = set()
        self.parse_schema(schema_string)

    def parse_schema(self, schema_string):
        # Parse the schema string into our schema representation (`schema_labels` and `schema_patterns`)
        schema_split = schema_string.split('), (')
        for entry in schema_split:
            entry = entry.replace('(', '').replace(')', '')
            start_label, rel_type, end_label = entry.split(', ')
            self.schema_labels.add(start_label)
            self.schema_labels.add(end_label)
            self.schema_patterns.add(to_schema_string('*', rel_type ,end_label))
            self.schema_patterns.add(to_schema_string(start_label, rel_type, '*'))
            self.schema_patterns.add(to_schema_string(start_label, '*' ,end_label))

    def should_reverse_pattern(self, rel_pattern, node_patterns):
        # Determine whether a `rel_pattern` needs to be reversed.

        rel_types = rel_pattern.types
        start_node = rel_pattern.start_node
        end_node = rel_pattern.end_node

        # If we spot an undirected relationship, no need to correct it.
        if rel_pattern.direction == Direction.BOTH:
            return False

        # Set start and end labels based on the direction of the relationship pattern.
        if rel_pattern.direction == Direction.RIGHT:
            start_labels = node_patterns[start_node].labels
            end_labels = node_patterns[end_node].labels
        if rel_pattern.direction == Direction.LEFT:
            end_labels = node_patterns[start_node].labels
            start_labels = node_patterns[end_node].labels

        # if start labels and end labels are the same (e.g. (:A)-[:X]->(:A)), we don't need to correct anything. 
        if start_labels == end_labels:
            return False

        # There are several cases in which we can fix the direction:
        # 1. The triple [(start label), (rel_type), (*)] does not exist in the schema, but the reverse does.
        # 2. The triple [(*), (rel_type), (end label)] does not exist in the schema, but the reverse does.
        # 3. The triple [(start label), (*), (end label)] does not exist in the schema, but the reverse does.

        # In case a triple does not exist, and neither does the reverse, it doesn't fit the schema, and we throw an error.

        # Case 1 - example triples of shape [(start label), (rel_type), (*)]
        for start in start_labels:
            if start in self.schema_labels:
                for type in rel_types:
                    entry = to_schema_string(start, type, '*')
                    reverse_entry = to_schema_string('*', type, start)
                    if entry not in self.schema_patterns:
                        if reverse_entry in self.schema_patterns:
                            return True
                        else:
                            raise Exception('Unable to fix relationship direction.')

        # Case 2 - example triples of shape [[(*), (rel_type), (end label)]
        for end in end_labels:
            if end in self.schema_labels:
                for type in rel_types:
                    entry = to_schema_string('*', type, end)
                    reverse_entry = to_schema_string(end, type, '*')
                    if entry not in self.schema_patterns:
                        if reverse_entry in self.schema_patterns:
                            return True
                        else:
                            raise Exception('Unable to fix relationship direction.')

         # Case 3 - example triples of shape [(start label), (*), (end label)]
        for start in start_labels:
            for end in end_labels:
                if start in self.schema_labels and end in self.schema_labels:
                    entry = to_schema_string(start, '*', end)
                    reverse_entry = to_schema_string(end, '*', start)
                    if entry not in self.schema_patterns:
                        if reverse_entry in self.schema_patterns:
                            return True
                        else:
                            raise Exception('Unable to fix relationship direction.')
        return False

    def reverse_relationship_pattern(self, pattern_string, direction):
        # Reverses a relationship pattern in the query.

        if direction == Direction.RIGHT:
            # TODO - do this better with a regex, or modify AST directly.
            pattern_string = pattern_string.replace("->(", "-(")
            pattern_string = pattern_string.replace(")-", ")<-")

        if direction == Direction.LEFT:
            # TODO - do this better with a regex, or modify AST directly.
            pattern_string = pattern_string.replace(")<-", ")-")
            pattern_string = pattern_string.replace("-(", "->(")
        return pattern_string

    def handle_relationship_pattern(self, query, rel_pattern, node_patterns):
        # Update the query if relationships need to be inverted. If not, the query stays the same.

        to_reverse: bool = self.should_reverse_pattern(rel_pattern, node_patterns)
        if to_reverse:
            pattern_string = rel_pattern.pattern_string
            reversed_pattern_string = self.reverse_relationship_pattern(
                pattern_string, rel_pattern.direction)
            return query.replace(pattern_string, reversed_pattern_string)
        return query


    def run(self, query) -> str:
        """
        Runs CypherGuard on an input string.
        Returns an output query, either original or modified with correct relationship directions.
        """
        node_patterns, relationship_patterns = extract_rel_patterns(query)
        for rel_pattern in dict.values(relationship_patterns):
            try:
                query = self.handle_relationship_pattern(query, rel_pattern, node_patterns)
            except:
                # If the direction cannot be fixed, just return an empty string as per the specification.
                return ''
            
        return query
