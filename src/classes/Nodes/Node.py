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
        self._name = self.ClassName

        #init properties
        for prop in kwargs.keys():
            setattr(self, prop, kwargs.get(prop))

    
    def __str__(self) -> str:
        return self.Name

    def _checkLock(self, property):
        if property in self._lockedProperties:
            raise Exception(f"Property '{property}' of {self.FullName} is locked.")

    def _addLock(self, property):
        if property not in self._lockedProperties:
            self._lockedProperties.append(property)


    ###### PROPERTIES ######

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, value: str):
        if type(value) != str:
            raise Exception("Type error: 'Name' must be a string.")

        self._name = value

    @property
    def FullName(self):
        fullName = self.Name
        curParent = self.Parent

        while curParent != None:
            fullName = curParent.Name + "." + fullName
            curParent = curParent.Parent

        return fullName

    @property
    def ClassName(self) -> str:
        return type(self).__name__
    
    @property
    def Children(self) -> list["Node"]:
        return self._children.copy()
    
    @property
    def Parent(self) -> Optional["Node"]:
        """
        Determines the hierarchical parent of this `Node`.
        """
        return self._parent
    
    @Parent.setter
    def Parent(self, value: Optional["Node"]):
        if type(value) != Node:
            raise Exception("Type error: 'Name' must be a string.")

        self._checkLock("Parent")
        self._parent = value


    ###### METHODS ######

    def Destroy(self):
        """
        Sets `self.Parent` to None and locks it, disconnects all connections, and calls `Destroy` on all child nodes.
        """

        self.Parent = None
        self._addLock("Parent")

        for child in self.Children:
            child.Destroy()
