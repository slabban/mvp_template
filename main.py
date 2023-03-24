#!/usr/bin/env python3

from model import concreteModel 
from view import ConcreteView
from presenter import concretePresenter
from services import concreteService




def main() -> None:
    
    model = concreteModel()
    service = concreteService(my_model=model)
    view = ConcreteView()
    presenter = concretePresenter(service=service, view=view)
    view.presenter = presenter
    service.attachPresenter(presenter=presenter)
    presenter.run()


if __name__ == "__main__":
    main()
