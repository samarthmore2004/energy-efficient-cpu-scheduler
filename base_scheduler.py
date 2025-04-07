class Scheduler:
    def __init__(self, tasks):
        self.tasks = tasks
    
    def run(self):
        raise NotImplementedError("Subclasses must implement run method")