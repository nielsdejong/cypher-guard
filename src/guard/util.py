from enum import Enum


class Direction(Enum):
    # Enum for Relationship pattern direction.
    RIGHT = 1
    LEFT = 2
    BOTH = 3

class SchemaEntry:
    start_label: str
    rel_type: str
    end_label: str

    def __init__(self, start_label, rel_type, end_label) -> None:
        self.start_label = start_label
        self.rel_type = rel_type
        self.end_label = end_label

class NodePattern:
    var_name: str
    labels: [str]

    def __init__(self, var_name, labels):
        self.var_name = var_name
        self.labels = labels

    
class RelationshipPattern:
    var_name: str
    start_node: str
    end_node: str
    direction: Direction
    types: [str]
    pattern_string: str
    
    def __init__(self, name, start_node, end_node, direction, types, pattern_string) -> None:
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.direction = direction
        self.types = types
        self.pattern_string = pattern_string
        print(pattern_string)
