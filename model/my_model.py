#!/usr/bin/env python3
from interfaces import IModel


class myModel(IModel):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def perform_business_logic(self):
        print("I am have performed some internal logic..")