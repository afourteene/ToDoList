from abc import ABC,abstractmethod


class RepositoryInterface(ABC):
    def __init__(self):
        self.tasks = []

    @abstractmethod
    def save(self, task_data):
        pass

    @abstractmethod
    def load(self, task_id):
        pass

    @abstractmethod
    def delete(self):
        pass
    
    @abstractmethod
    def getAll(self):
        pass
