from enum import Enum


class Direction(Enum):
    # Simple enum for relationship pattern direction.
    RIGHT = 1
    LEFT = 2
    BOTH = 3


class NodePattern:
    # A node pattern in a query, i.e. `(n)`, `(n:Person)`, or `(n:Person:Actor)`
    var_name: str
    labels: [str]

    def __init__(self, var_name, labels):
        self.var_name = var_name
        self.labels = labels


class RelationshipPattern:
    # A relationship pattern in a query, i.e. `(n)-[a:ACTED_IN]->(m)` or  `(n)-[:ACTED_IN|DIRECTED]->(m)`
    var_name: str           # variable name, i.e. `a`
    start_node: str         # start node name, i.e. `n`
    end_node: str           # end node name, i.e. `m`
    direction: Direction    # direction of the pattern.
    types: [str]            # list of relationship types used in the pattern.
    # a stringified version of the pattern, as in the original query.
    pattern_string: str

    def __init__(self, name, start_node, end_node, direction, types, pattern_string) -> None:
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.direction = direction
        self.types = types
        self.pattern_string = pattern_string


def to_schema_string(start, type, end):
    # Helper function for encoding a schema pattern into a string.
    return start + ',' + type + ',' + end
