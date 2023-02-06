from interfaces import IServices
from model.interfaces import IModel

class myServices(IServices):
    def __init__(self, my_model: IModel) -> None:
        super().__init__(my_model)
        
    def fetch_data(self):
        print("Fetching data that will be assigned to the model and shared with the presenter")

    def push_data(self, data: dict):
        print("Pushing local data to a repository")


if __name__ == "__main__":
    my_model = IModel()

