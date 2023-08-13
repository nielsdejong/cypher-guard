from guard.util import Direction, SchemaEntry
from guard.parser.parser import extract_rel_patterns


class CypherGuard():
    schema: set

    def __init__(self, schema_string) -> None:
        self.schema = set()
        self.parse_schema(schema_string)

        # Parse the schema string into our schema representation.
        
    def parse_schema(self, schema_string):
        schema_split = schema_string.split('), (')
        for entry in schema_split:
            entry = entry.replace('(', '').replace(')', '')
            start_label, rel_type, end_label = entry.split(', ')
            self.schema.add('*' + ',' + rel_type + ',' + end_label)
            self.schema.add(start_label + ',' + rel_type + ',' '*')

    def should_reverse_pattern(self, rel_pattern, node_patterns):
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

        # There are two cases in which we can fix the direction:

        # 1. The triple [(start label), (rel_type), (*)] does not exist in the schema
        for start in start_labels:
            for type in rel_types:
                entry = start+','+type+','+'*'
                reverse_entry = '*'+','+type+','+start
                if entry not in self.schema and reverse_entry in self.schema:
                    return True

        # 2. The triple [(*), (rel_type), (end label)] does not exist in the schema
        for end in end_labels:
            for type in rel_types:
                entry = '*'+','+type+','+end
                reverse_entry = end+','+type+','+'*'
                if entry not in self.schema and reverse_entry in self.schema:
                    return True

        return False

    def reverse_relationship_pattern(self, pattern_string, direction):
        """
        We reverse a relationship pattern in the query.
        """

        if direction == Direction.RIGHT:
            # TODO - do this better with a regex.
            pattern_string = pattern_string.replace("->(", "-(")
            pattern_string = pattern_string.replace(")-", ")<-")

        if direction == Direction.LEFT:
            # TODO - do this better with a regex.
            pattern_string = pattern_string.replace(")<-", ")-")
            pattern_string = pattern_string.replace("-(", "->(") 
        return pattern_string

    def run(self, input) -> str:
        """
        Runs CypherGuard on an input string.

        """
        node_patterns, relationship_patterns = extract_rel_patterns(input)
        output = input # deep copy input as a new output...
        for rel_pattern in dict.values(relationship_patterns):
            to_reverse: bool = self.should_reverse_pattern(rel_pattern, node_patterns)
            if to_reverse:
                pattern_string = rel_pattern.pattern_string
                reversed_pattern_string = self.reverse_relationship_pattern(pattern_string, rel_pattern.direction)
                output = output.replace(pattern_string, reversed_pattern_string)
        return output


