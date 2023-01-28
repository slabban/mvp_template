#!/usr/bin/env python3

from common.interfaces import IPresenterView

class view (object):
  def __init__(self, view : IPresenterView) -> None:
    self.view = view