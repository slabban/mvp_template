#!/usr/bin/env python3

from abc import ABC, abstractmethod

class IViewController(ABC):
    '''The IView Controller interface acts as the abstracted
    medium between the view and the presenter. It handles operations 
    such as populating layouts and views and receiving user actions
    '''