from services.interfaces import IServices
from model.interfaces import IModel
from presenter.interfaces import IPresenter


class concreteService(IServices):
    def __init__(self, my_model: IModel) -> None:
        self.model = my_model
        
    def send_data(self):
        data = self.model.get_data()
        self._notify(data)
    
    def get_data(self):
        return self.model.get_data()
    
    def update_model(self, data):
        self.model.set_data(data)

    def attach(self, presenter : IPresenter):
        self.presenter = presenter

    def detach(self):
        self.presenter = None

    def _notify(self, data):
        self.presenter.update_view(data)

    def push_data(self, data: dict):
        print("Pushing local data to a repository")


