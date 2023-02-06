#!/usr/bin/env python3

from abc import ABC, abstractmethod
from model.interfaces import IModel 

class IServices(ABC):
    """The Services interface acts as the medium between the presenter and the mode. 
    It's purpose is to encapsulate the model features as
    services that would fetch information from repositories and databases"""
    def __init__(self, my_model: IModel) -> None:
        self.my_model = my_model

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def push_data(self, data: dict):
        pass
