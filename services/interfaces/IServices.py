#!/usr/bin/env python3

from abc import ABC, abstractmethod
from model.interfaces import IModel

class IServices(ABC):
    """The Services interface acts as the medium between the presenter and the mode. 
    It's purpose is to encapsulate the model features as
    services that would fetch information from repositories and databases"""

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def push_data(self, data: dict):
        pass
