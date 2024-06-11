import sqlite3

class Author:
    def __init__(self, name):
        self.name = name
        self._id = None

        # Create a new entry in the authors table
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self.name = value

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._id = None

        # Create a new entry in the magazines table
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self.name = value

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self.category = value

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.author_id = author.id
        self.magazine_id = magazine.id

        # Create a new entry in the articles table
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)", (self.author_id, self.magazine_id, self.title))
        conn.commit()
        conn.close()

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self.title = value

    @property
    def author(self):
        return self.author

    @property
    def magazine(self):
        return self.magazine