class RepositoryInterface(ABC):
    def __init__(self):
        self.tasks = []

    def save(self, task_data):
        pass


    def load(self, task_id):
        pass


    def getAll(self):
        pass
