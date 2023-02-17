#!/usr/bin/env python3

from model.interfaces import IModel
from presenter.interfaces import IPresenter


class concreteModel(IModel):
    def __init__(self) -> None:
        super().__init__()
        self.data = None
    
    def get_data(self):
        return "Model Data"

    def set_data(self, data):
        self.data = data
            