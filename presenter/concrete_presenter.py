#!/usr/bin/env python3

from presenter.interfaces import IPresenter
from services.interfaces import IServices
from view.interfaces import IView

from common.interfaces import ICommand

 
class concretePresenter(IPresenter):

    def __init__(self, service: IServices, view: IView):
        super().__init__(service, view)
        self.service = service
        self.view = view
        self.updatemodel_command : ICommand = None   
    
    def update_view(self, data):
        self.view.display_data(data)

    def update_model(self, data):
        self.updatemodel_command.execute()
            
    def run(self):
        self.view.start()
    
