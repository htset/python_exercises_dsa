class Task:
    def __init__(self, description=None, priority=0):
        self.description = description
        self.priority = priority
        self.next = None
    