#!/usr/bin/env python3




class IObserver(ABC):
    """used to notify the
    presenter of changes in the model and to update the view accordingly.
    The model acts as the IObservable and the presenter and view are observers."""

    @abstractmethod
    def update(self, IObservable, args=None):
        pass


class IObservable(ABC):
    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, args=None):
        pass
