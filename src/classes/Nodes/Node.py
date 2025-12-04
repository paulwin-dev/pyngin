from typing import Any, Optional

from .EngineObject import EngineObject

class Node(EngineObject):
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
            fullName = curParent.name + "." + fullName
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
        if type(value) != Node:
            raise Exception("Type error: 'Name' must be a string.")

        self._checkLock("Parent")
        self._parent = value


    ###### METHODS ######

    def destroy(self):
        """
        Sets `self.Parent` to None and locks it, disconnects all connections, and calls `Destroy` on all child nodes.
        """

        self.parent = None
        self._addLock("Parent")

        for child in self.children:
            child.destroy()
