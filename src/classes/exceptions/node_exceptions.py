from classes.exceptions.engine_exception import EngineError


class NodeNotFoundError(EngineError):
    def __init__(self, path):
        super().__init__(f"Node not found: '{path}'.")

class UnexpectedNodeTypeError(EngineError):
    def __init__(self, path, expected, actual):
        super().__init__(
            f"Expected node '{path}' to be of type {expected}, got {actual}."
        )