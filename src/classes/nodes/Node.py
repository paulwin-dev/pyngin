from typing import Any, Optional, Type, TypeVar

from classes.exceptions.node_exceptions import NodeNotFoundError, UnexpectedNodeTypeError

from ..base.engine_base import EngineBase

TNode = TypeVar("TNode", bound="Node")

class Node(EngineBase):
    """
    Represents a node in the hierarchical structure.
    """

    def __init__(self, **kwargs):
        self._children = []
        self._parent = None
        self._lockedProperties = []
        self._name = self.class_name

        #init properties
        for prop in kwargs.keys():
            setattr(self, prop, kwargs.get(prop))

    
    def __str__(self) -> str:
        return self.name

    def _checkLock(self, property):
        if property in self._lockedProperties:
            raise Exception(f"Property '{property}' of {self.full_name} is locked.")

    def _addLock(self, property):
        if property not in self._lockedProperties:
            self._lockedProperties.append(property)


    ###### PROPERTIES ######

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) != str:
            raise Exception("Type error: 'Name' must be a string.")

        self._name = value

    @property
    def full_name(self):
        fullName = self.name
        curParent = self.parent

        while curParent != None:
            fullName = curParent.name + "/" + fullName
            curParent = curParent.parent

        return fullName

    @property
    def class_name(self) -> str:
        return type(self).__name__
    
    @property
    def children(self) -> list["Node"]:
        return self._children.copy()
    
    @property
    def parent(self) -> Optional["Node"]:
        """
        Determines the hierarchical parent of this `Node`.
        """
        return self._parent
    
    @parent.setter
    def parent(self, value: Optional["Node"]):
        self._checkLock("Parent")

        if not isinstance(value, Node) and value != None:
            raise Exception("Type error: 'Parent' must be a node.")        

        if self.parent != None:
            self.parent._children.remove(self)

        self._parent = value

        if self._parent != None:
            self._parent._children.append(self)


    ###### METHODS ######
    def _get_node_by_name(self, name):
        for node in self.children:
            if node.name == name:
                return node
        
        return None

    def get_node(self, name: str, node_type: Type[TNode] | None = None) -> TNode | "Node":
        node = self._get_node_by_name(name)

        if node is None:
            raise NodeNotFoundError(self.full_name+"/"+name)
        
        if node_type is not None and not isinstance(node, node_type):
            raise UnexpectedNodeTypeError(node.full_name, node_type.__name__, type(node).__name__)
        
        return node

    def get_node_or_none(self, name: str, node_type: Type[TNode] | None = None) -> Optional[TNode | "Node"]:
        node = self._get_node_by_name(name)

        if node is None:
            return None

        return node

    def destroy(self):
        """
        Sets `self.Parent` to None and locks it, disconnects all connections, and calls `Destroy` on all child nodes.
        """

        self.parent = None
        self._addLock("Parent")

        for child in self.children:
            child.destroy()
