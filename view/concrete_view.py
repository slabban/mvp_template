#!/usr/bin/env python3
from presenter.interfaces import IPresenter
from view.interfaces import IView
import tkinter as tk



class ConcreteView(IView):
    def __init__(self):
        super().__init__()

    
    def init_gui(self):
        self._root = tk.Tk()
        self._label = tk.Label(text="Test Gui")
        self._label.pack()

    def start(self):
        self.init_gui()
        self.mainloop()
        
    def mainloop(self):
        self._root.mainloop()
    
    def display_data(self, data):
        self.viewed_data = tk.Label(text=data)
        self.viewed_data.pack()

    def set_data(self, data):
        self.presenter.update_model(data)
    
