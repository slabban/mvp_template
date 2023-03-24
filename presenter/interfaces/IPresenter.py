#!/usr/bin/env python3

from abc import ABC, abstractmethod

from services.interfaces import IServices
from view.interfaces import IView


class IPresenter(ABC):
    """Presenter acts as the medium between the view and model.
    It is accepts abstractions of the model and view as injected dependencies.
    The model and view should have no knowledge of each other as they are mediated
    bertween the presenter"""

    def __init__(self, service: IServices, view: IView):
        self.service = service
        self.view = view   

    @abstractmethod
    def update_view(self):
        pass
    
    @abstractmethod
    def update_model(self):
        pass

    @abstractmethod
    def run(self):
        pass
