#!/usr/bin/env python3

from abc import ABC, abstractmethod

class IObserver(ABC):
  """used to notify the 
  presenter of changes in the model and to update the view accordingly. 
  The model acts as the subject and the presenter and view are observers."""
  @abstractmethod
  def update(self, subject, args=None):
      pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self, args=None):
        pass