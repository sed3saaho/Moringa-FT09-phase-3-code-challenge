class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be an integer")
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) < 50 or len(value) > 5000:
            raise ValueError("Content must be between 50 and 5000 characters")
        self._content = value

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Author ID must be an integer")
        self._author_id = value

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Magazine ID must be an integer")
        self._magazine_id = value

    @classmethod
    def create(cls, title, content, author_id, magazine_id):
       new_article = cls(None, title, content, author_id, magazine_id)

       return new_article

    @classmethod
    def get(cls, article_id):
        return cls(article_id, "Test Title", "Test Content", 1, 1)
    @classmethod
    def all(cls):
        return [cls(1, "Test Title", "Test Content", 1, 1), cls(2, "Test Title", "Test Content", 1, 1), cls(3, "Test Title", "Test Content", 1, 1)]
    @classmethod
    def update(cls, article_id, title=None, content=None):
        article = cls.get(article_id)
        if title:
            article.title = title
        if content:
            article.content = content
        
        return article

    @classmethod
    def delete(cls, article_id):
        # Delete an Article instance by its ID from the database
        # Assuming you have a database connection object named `conn`
        with conn.cursor() as cursor:
             cursor.execute("DELETE FROM articles WHERE id = %s", (article_id,))
             conn.commit()