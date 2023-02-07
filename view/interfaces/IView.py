#!/usr/bin/env python3

from abc import ABC, abstractmethod
from presenter.interfaces import IPresenter


class IView(ABC):
    def __init__(self) -> None:
        self.presenter: IPresenter = None

    @abstractmethod
    def update_view(self, data: dict):
        pass

    @abstractmethod
    def get_user_input(self) -> dict:
        pass

