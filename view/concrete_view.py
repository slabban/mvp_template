#!/usr/bin/env python3
from presenter.interfaces import IPresenter
from view.interfaces import IView
import tkinter as tk



class ConcreteView(IView):
    def __init__(self) -> None:
        self.presenter : IPresenter 
    
    def init_gui(self):
        self._root = tk.Tk()
        self._label = tk.Label(text=self.update_view())
        self._label.pack()

    def start(self):
        self.init_gui()
        self.mainloop()
        
    def mainloop(self):
        self._root.mainloop()
    
    def update_view(self):
        return self.presenter.update_view()
    
