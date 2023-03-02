#!/usr/bin/env python3

from abc import ABC, abstractmethod
from model.interfaces import IModel
from presenter.interfaces import IPresenter

class IServices(ABC):
    """The Services interface acts as the medium between the presenter and the mode. 
    It's purpose is to encapsulate the model features as
    services that would fetch information from repositories and databases"""

    #TODO: encapsulate the repository fetching logic within a seprate class that services can access
    #TODO: Initialize constructors for all interfaces
    def __init__(self, my_model: IModel) -> None:
        self.model = my_model
        self.presenter : IPresenter = None 

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
    def attachPresenter(self, presenter : IPresenter): 
        pass

    @abstractmethod
    def detachPresenter(self):
        pass
  
    @abstractmethod
    def notifyPresenter(self):
        pass