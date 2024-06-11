from database.connection import get_db_connection

class Author:
    all = {}

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __repr__(self):
        return f'<Author {self.id} {self.name}>'

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after initialization")
        else:
            if isinstance(new_name, str):
                if len(new_name) > 0:
                    self._name = new_name

    def save(self):
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            INSERT INTO authors (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        conn.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        author = cls(None, name)
        author.save()
        return author

    def get_author_id(self):
        return self.id

    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            SELECT ar.*
            FROM articles ar
            INNER JOIN authors a ON ar.author = a.id
            WHERE a.id = ?
        """
        CURSOR.execute(sql, (self.id,))
        article_data = CURSOR.fetchall()
        articles = [Article(*row) for row in article_data]
        return articles

    def magazines(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            SELECT DISTINCT m.*
            FROM magazines m
            INNER JOIN articles ar ON ar.magazine = m.id
            INNER JOIN authors a ON ar.author = a.id
            WHERE a.id = ?
        """
        CURSOR.execute(sql, (self.id,))
        magazine_data = CURSOR.fetchall()
        magazines = [Magazine(*row) for row in magazine_data]
        return magazines

    @classmethod
    def instance_from_db(cls, row):
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
        else:
            author = cls(row[0], row[1])
            cls.all[author.id] = author
        return author

    @classmethod
    def list_all_authors(cls):
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            SELECT *
            FROM authors
        """
        CURSOR.execute(sql)
        author_data = CURSOR.fetchall()
        authors = [cls.instance_from_db(row) for row in author_data]
        return authors