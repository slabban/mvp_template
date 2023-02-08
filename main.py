#!/usr/bin/env python3

from model.concrete_model import concreteModel 
from view.concrete_view import MyView
from presenter.concrete_presenter import concretePresenter
from services.concrete_services import concreteService




def main() -> None:
    
    model = concreteModel()
    service = concreteService(my_model=model)
    view = MyView()
    presenter = concretePresenter(service=service, view=view)
    view.presenter = presenter
    presenter.run()


if __name__ == "__main__":
    main()
