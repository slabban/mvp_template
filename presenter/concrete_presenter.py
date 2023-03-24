#!/usr/bin/env python3

from .interfaces import IPresenter
from services.interfaces import IServices
from view.interfaces import IView

 
class concretePresenter(IPresenter):

    def __init__(self, service: IServices, view: IView):
        super().__init__(service, view)

    
    def update_view(self, data):
        self.view.display_data(data)

    def update_model(self, data):
        self.service.update_model(data)
            
    def run(self):
        self.view.start()
    
