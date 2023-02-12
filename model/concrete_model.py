#!/usr/bin/env python3

from model.interfaces import IModel


class concreteModel(IModel):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def get_data(self):
        return "Model Data"