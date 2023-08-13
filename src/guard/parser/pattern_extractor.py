

from guard.util import Direction, RelationshipPattern, NodePattern
from guard.generated import CypherParser, CypherParserListener


class PatternExtractor(CypherParserListener.CypherParserListener):
    """
    Extracts patterns from the Cypher query.
    """

    query: str
    node_patterns: dict
    rel_patterns: dict

    def __init__(self, query):
        self.query = query
        self.node_patterns = {}
        self.rel_patterns = {}

    def enterNodePattern(self, ctx):
        # Default variable name for anonymous nodes is based on their index in the query.
        var_name = 'ANON_' + str(ctx.start.start)

        for child in ctx.children:
            # When we encounter the node variable name, remember it in context of the pattern.
            if type(child) == CypherParser.CypherParser.VariableContext:
                var_name = child.getText()

            # When we encounter a label, and we have a var name in scope, store the mapping (e.g. n:Person).
            if type(child) == CypherParser.CypherParser.LabelExpressionContext:
                label = child.getText()[1:]
                if not var_name in self.node_patterns:
                    self.node_patterns[var_name] = NodePattern(var_name=var_name, labels=[])
                self.node_patterns[var_name].labels.append(label)

        if not var_name in self.node_patterns:
            self.node_patterns[var_name] = NodePattern(var_name=var_name, labels=[])

    # Enter a path pattern.
    # A path pattern consists of 1...n repeats of blocks shaped (a)-[b]->(c)
    # We need to find each block and extract relevant information from it.
    def enterPathPatternAtoms(self, ctx):
        for index, child in enumerate(ctx.children):
            if type(child) == CypherParser.CypherParser.MaybeQuantifiedRelationshipPatternContext:
                start_node_context = ctx.children[index-1]
                rel_pattern_context = ctx.children[index].children[0]
                end_node_context = ctx.children[index+1]
                self.extractRelDetailsFromPathPattern(start_node_context, rel_pattern_context, end_node_context)

        pass

    # We found a pattern (a)-[b]->(c). Extract needed information and store it in our dictionary.
    def extractRelDetailsFromPathPattern(self, start_node_context, rel_pattern_context, end_node_context):
        # Determine the variable name of the start node.
        start_index = start_node_context.start.start
        start_node_var_name = 'ANON_' + str(start_index)
        for child in start_node_context.children:
            if type(child) == CypherParser.CypherParser.VariableContext:
                start_node_var_name = child.getText()

        # Determine the variable name of the end node.
        end_index = end_node_context.stop.stop
        end_node_var_name = 'ANON_' + str(end_node_context.start.start)
        for child in end_node_context.children:
            if type(child) == CypherParser.CypherParser.VariableContext:
                end_node_var_name = child.getText()

        # Determine the variable name, type(s), indexes of the arrow symbols, and directions of the relationship.
        rel_var_name =  'ANON_' + str(rel_pattern_context.start.start)
        rel_direction = Direction.BOTH
        rel_types = []
        arrow_symbol_string_indexes = []

        for child in rel_pattern_context.children:
            if type(child) == CypherParser.CypherParser.VariableContext:
                rel_var_name = child.getText()
            if type(child) == CypherParser.CypherParser.LabelExpressionContext:
                rel_types = child.getText()[1:].split("|")
            if type(child) == CypherParser.CypherParser.RightArrowContext:
                rel_direction = Direction.RIGHT
            if type(child) == CypherParser.CypherParser.LeftArrowContext:
                rel_direction = Direction.LEFT
            if type(child) == CypherParser.CypherParser.ArrowLineContext:
                arrow_symbol_string_indexes.append(child.start.start)

        self.rel_patterns[rel_var_name] = RelationshipPattern(
            name=rel_var_name,
            types=rel_types,
            start_node=start_node_var_name,
            end_node=end_node_var_name,
            direction=rel_direction,
            pattern_string=self.query[start_index:end_index+1])