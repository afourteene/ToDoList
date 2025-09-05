from core.interfaces import RepositoryInterface


class saveToFile(RepositoryInterface):

    def __init__(self):
        self.tasks = []

    def save(self, task_data):

        return



    def load(self):

        return True

    def delete(self, task_id):

        return True

    def getAll(self, task_id):

        return self.tasks
    
