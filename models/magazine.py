class Magazine:
    def init(self, id, name, category = None):
        self._id = id
        self._name = name
        self._category = category

@property
def id(self):
    return self._id

@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    if isinstance(value, str) and 2 <= len(value) <= 16:
        self._name = value
    else:
        raise ValueError("Name must be a string between 2 and 16 characters")

@property
def category(self):
    return self._category

@category.setter
def category(self, value):
    if isinstance(value, str) and len(value) > 0:
        self._category = value
    else:
        raise ValueError("Category must be a non-empty string")

def create_magazine(self, cursor):
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self._name, self._category))
    self._id = cursor.lastrowid
    return cursor

@classmethod
def get_all_magazines(cls, cursor):
    cursor.execute("SELECT * FROM magazines")
    all_magazines = cursor.fetchall()
    return [cls(magazine_data[0], magazine_data[1], magazine_data[2]) for magazine_data in all_magazines]

def articles(self, cursor):
    cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self._id,))
    articles_data = cursor.fetchall()
    return articles_data

def contributors(self, cursor):
    cursor.execute("""
        SELECT authors.*
        FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
    """, (self._id,))
    contributors_data = cursor.fetchall()
    return contributors_data

def article_titles(self, cursor):
    cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self._id,))
    titles = [row[0] for row in cursor.fetchall()]
    return titles if titles else None

def contributing_authors(self, cursor):
    cursor.execute("""
        SELECT authors., COUNT() AS article_count
        FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
        GROUP BY authors.id
        HAVING article_count > 2
    """, (self._id,))
    authors_data = cursor.fetchall()
    return authors_data if authors_data else None

def _repr_(self):
    return f"Magazine(id={self._id}, name='{self._name}', category='{self._category}')"