#!/usr/bin/env python3

from abc import ABC, abstractmethod


class IView(ABC):

    @abstractmethod
    def update_view(self):
        pass
    
    @abstractmethod
    def start(self):
        pass

