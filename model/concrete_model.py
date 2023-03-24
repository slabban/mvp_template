#!/usr/bin/env python3

from .interfaces import IModel



class concreteModel(IModel):
    def __init__(self) -> None:
        super().__init__()
        self.data = None
    
    def get_data(self):
        return "Model Data"

    def set_data(self, data):
        self.data = data
            