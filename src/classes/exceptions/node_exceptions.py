from classes.exceptions.engine_exception import EngineError


class NodeNotFoundError(EngineError):
    def __init__(self, path):
        super().__init__(f"Node not found: '{path}'.")

class UnexpectedNodeTypeError(EngineError):
    def __init__(self, path, expected, actual):
        super().__init__(
            f"Expected node '{path}' to be of type {expected}, got {actual}."
        )

class PropertyNotFoundError(EngineError):
    def __init__(self, path, property_name, class_name) -> None:
        super().__init__(
            f"Property {property_name} not found in {class_name} '{path}'"
        )