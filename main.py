#!/usr/bin/env python3

from model.my_model import MyModel
from view.my_view import MyView
from presenter.my_presenter import MyPresenter

if __name__ == '__main__':
    model = MyModel()
    view = MyView()
    presenter = MyPresenter(model, view)
    view.presenter = presenter
    view.show()