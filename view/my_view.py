#!/usr/bin/env python3
from presenter.interfaces import IPresenter
from view.interfaces import IView



class MyView(IView):
    def __init__(self) -> None:
        super().__init__()
    
    def get_user_input(self) -> dict:
        print("getting the user input")
    
    def update_view(self, data: dict):
        print("updating the gui")
    
