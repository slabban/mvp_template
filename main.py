#!/usr/bin/env python3

from model.my_model import myModel 
from view.my_view import MyView
from presenter.my_presenter import MyPresenter
from services.my_services import myServices




def main() -> None:
    
    model = myModel()
    service = myServices(my_model=model)
    view = MyView()
    presenter = MyPresenter(service=service, view=view)
    view.presenter = presenter
    presenter.run()


if __name__ == "__main__":
    main()
