class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise ValueError("ID must be an integer")
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 20:
            raise ValueError("Name must be a string between 2 and 20 characters")
        self._name = name