from common.interfaces import ICommand
from interfaces import IServices

class UpdateModelCommand(ICommand):
    def __init__(self, service : IServices, updated_data):
        self._service = service
        self._new_value = updated_data
        self._old_value = None

    def execute(self):
        self._old_value = self._service.get_data()
        self._service.model.set_data(self._new_value)

    def undo(self):
        self._service.model.set_data(self._old_value)  