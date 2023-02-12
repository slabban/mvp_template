#!/usr/bin/env python3

from abc import ABC, abstractmethod


class IModel(ABC):
    """The IModel interface represents the model as a facade that
    governs the internal functions of the model. It is meant to be a standalone representative
    of the model package"""

    @abstractmethod
    def get_data(self):
        pass
