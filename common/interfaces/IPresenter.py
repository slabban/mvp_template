#!/usr/bin/env python3

from abc import ABC, abstractmethod
from IModel import IModel
from IView import IView
from IObserver import IObserver
from ICommand import ICommand

class IPresenter(ABC):
  """Presenter acts as the middleman between the view and model
  It is accepts abstractions of the model and view as injected dependencies"""
  def __init__(self, model: 'IModel', view: 'IView'):
      self._model = model
      self._view = view


  @abstractmethod
  def update_view(self):
      pass

  @abstractmethod
  def update_model(self):
      pass
