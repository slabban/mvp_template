#!/usr/bin/env python3
from abc import ABC, abstractmethod

class ICommand(ABC):
    """ used in the presenter to encapsulate a request as an object, which can be 
    passed to other objects to execute the request. 
    This allows for decoupling the objects that invoke the operation from the objects that perform the operation."""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
