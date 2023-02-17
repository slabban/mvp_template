from services.interfaces import IServices
from model.interfaces import IModel
from presenter.interfaces import IPresenter


class concreteService(IServices):
    def __init__(self, my_model: IModel) -> None:
        self.model = my_model
        
    def set_data(self):
        data = self.model.get_data()
        self.notify(data)
    
    def update_model(self, data):
        self.model.set_data(data)

    def push_data(self, data: dict):
        print("Pushing local data to a repository")

    def attach(self, presenter : IPresenter):
        self.presenter = presenter

    def detach(self):
        self.presenter = None

    def notify(self, data):
        self.presenter.update_view(data)



