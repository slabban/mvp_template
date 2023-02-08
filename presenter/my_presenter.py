#!/usr/bin/env python3

from presenter.interfaces import IPresenter
from services.interfaces import IServices
from view.interfaces import IView

class MyPresenter (IPresenter):

    def __init__(self, service: IServices, view: IView):
        super().__init__(service, view)    
    # def __init__(self, s: IModel, view: IView):
    #     super().__init__(model, view)
    
    def update_view(self):
        print("updating the gui")
        #self._view.update_view()


    def update_model(self):
        print("updating model")
        # self._model.perform_business_logic()
            
    def run(self):
        print("placeholder for some main task that runs the gui")
    
