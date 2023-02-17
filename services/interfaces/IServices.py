#!/usr/bin/env python3

from abc import ABC, abstractmethod
from model.interfaces import IModel

class IServices(ABC):
    """The Services interface acts as the medium between the presenter and the mode. 
    It's purpose is to encapsulate the model features as
    services that would fetch information from repositories and databases"""

    #TODO: encapsulate the repository fetching logic within a seprate class that services can access
    #TODO: Initialize constructors for all interfaces

    @abstractmethod
    def set_data(self):
        pass

    @abstractmethod
    def update_model(self):
        pass

    @abstractmethod
    def push_data(self, data: dict):
        pass

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass
  
    @abstractmethod
    def notify(self):
        pass