from services.interfaces import IServices
from model.interfaces import IModel


class concreteService(IServices):
    def __init__(self, my_model: IModel) -> None:
        self.model = my_model
        
    def fetch_data(self):
        return self.model.get_data()
    
    def push_data(self, data: dict):
        print("Pushing local data to a repository")



