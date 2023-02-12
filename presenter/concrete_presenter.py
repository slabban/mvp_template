#!/usr/bin/env python3

from presenter.interfaces import IPresenter
from services.interfaces import IServices
from view.interfaces import IView

 
class concretePresenter(IPresenter):

    def __init__(self, service: IServices, view: IView):
        super().__init__(service, view)
        self.service = service
        self.view = view   
    
    def update_view(self):
        return self.service.fetch_data()

    def update_model(self):
        self.service.fetch_data()
            
    def run(self):
        self.view.start()
    