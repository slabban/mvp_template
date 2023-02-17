#!/usr/bin/env python3

from abc import ABC, abstractmethod


class IView(ABC):

    @abstractmethod
    def display_data(self):
        pass
    
    @abstractmethod
    def start(self):
        pass

