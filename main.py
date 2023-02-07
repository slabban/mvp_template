#!/usr/bin/env python3

from model.my_model import myModel 
from view.my_view import MyView
from presenter.my_presenter import MyPresenter



def main() -> None:
    model = myModel()
    view = MyView()
    presenter = MyPresenter(model=model, view=view)
    view.presenter = presenter
    presenter.run()


if __name__ == "__main__":
    main()
