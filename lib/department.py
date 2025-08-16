from __init__ import CURSOR, CONN

class Department:
    all = {}  # Object cache
    
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    # ... [All ORM methods shown in the lesson] ...