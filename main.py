#!/usr/bin/env python3

from model.concrete_model import concreteModel 
from view.concrete_view import ConcreteView
from presenter.concrete_presenter import concretePresenter
from services.concrete_services import concreteService

from services.concrete_command import UpdateModelCommand


def main() -> None:
    
    model = concreteModel()
    service = concreteService(my_model=model)
    view = ConcreteView()
    presenter = concretePresenter(service=service, view=view)
    
    view.presenter = presenter
    service.attach(presenter=presenter)
    presenter.run()


if __name__ == "__main__":
    main()
