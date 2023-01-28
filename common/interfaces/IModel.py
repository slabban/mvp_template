#!/usr/bin/env python3

from abc import ABC, abstractmethod

class IModel(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data: dict):
        pass