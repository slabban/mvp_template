#!/usr/bin/env python3

from abc import ABC, abstractmethod

class IProvider(ABC):
    """The IModelProvider interface acts as the medium between the presenter and the model
    and has direct access to the model. It's purpose is to encapsulate the model features as
    services that would fetch information from repositories and databases"""
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data: dict):
        pass
