from database.connection import get_db_connection

class Magazine:
    all = {}

    def __init__(self, id, name=None, category=None):
        self._id = id
        self._name = name
        self._category = category

    def __repr__(self):
        return f'<Magazine {self.id} {self.name} {self.category}>'

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
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO magazines (name, category)
            VALUES (?,?)
        """
        cursor.execute(sql, (self.name, self.category))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, category):
        magazine = cls(None, name, category)
        magazine.save()
        return magazine

    def get_magazine_id(self):
        return self.id

    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT ar.*
            FROM articles ar
            INNER JOIN magazines m ON ar.magazine = m.id
            WHERE m.id = ?
        """
        cursor.execute(sql, (self.id,))
        article_data = cursor.fetchall()
        articles = [Article(*row) for row in article_data]
        return articles

    def contributors(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT DISTINCT a.*
            FROM authors a
            INNER JOIN articles ar ON ar.author = a.id
            INNER JOIN magazines m on ar.magazine = m.id
            WHERE m.id = ?
        """
        cursor.execute(sql, (self.id,))
        author_data = cursor.fetchall()
        authors = [Author(*row) for row in author_data]
        return authors

    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT ar.title
            FROM articles ar
            INNER JOIN magazines m ON ar.magazine = m.id
            WHERE m.id = ?
        """
        cursor.execute(sql, (self.id,))
        article_data = cursor.fetchall()
        if not article_data:
            return None
        titles = [row[0] for row in article_data]
        return titles

    @property
    def contributing_authors(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            SELECT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id, authors.name
            HAVING COUNT(articles.id) > 2
        '''
        cursor.execute(sql, (self.id,))
        contributing_authors_data = cursor.fetchall()
        conn.close()
        return [Author(author['id'], author['name']) for author in contributing_authors_data]
    @classmethod
    def instance_from_db(cls, row):
        """Return a Magazine object having the attribute values from the table row."""
        magazine = cls.all.get(row[0])
        if magazine:
            magazine.name = row[1]
            magazine.category = row[2]
        else:
            magazine = cls(row[1], row[2])
            magazine.id = row[0]
            cls.all[magazine.id] = magazine
        return magazine
    
    @classmethod
    def list_all_magazines(cls):
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            SELECT *
            FROM magazines
        """

        CURSOR.execute(sql)
        magazine_data = CURSOR.fetchall()

        magazines = []
        for row in magazine_data:
            magazines.append(cls.instance_from_db(row))
        return magazines