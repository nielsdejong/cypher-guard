from enum import Enum


class Direction(Enum):
    # Enum for Relationship pattern direction.
    RIGHT = 1
    LEFT = 2
    BOTH = 3


class RelationshipPattern:
    var_name: str
    start_node: str
    end_node: str
    direction: Direction
    types: [str]
    arrow_symbol_string_indexes: [int]

    def __init__(self, name, start_node, end_node, direction, types, arrow_symbol_string_indexes) -> None:
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.direction = direction
        self.types = types
        self.arrow_symbol_string_indexes = arrow_symbol_string_indexes
