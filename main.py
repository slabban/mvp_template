#!/usr/bin/env python3

from model.my_model import MyModel
from view.my_view import MyView
from presenter.my_presenter import MyPresenter



def main() -> None:
    model = MyModel()
    view = MyView()
    presenter = MyPresenter(model, view)
    view.presenter = presenter
    presenter.run()


if __name__ == "__main__":
    main()
