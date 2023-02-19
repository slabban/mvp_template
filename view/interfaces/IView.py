#!/usr/bin/env python3

from abc import ABC, abstractmethod
from presenter.interfaces import IPresenter


class IView(ABC):

    def __init__(self):
        self.presenter : IPresenter = None 

    @abstractmethod
    def display_data(self):
        pass
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def set_data(self):
        pass

