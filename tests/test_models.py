import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation_valid(self):
        """Test Author creation with valid data."""
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation_valid(self):
        """Test Article creation with valid data."""
        # Providing longer content for testing
        article = Article(1, "Test Title", "A" * 50, 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation_valid(self):
        """Test Magazine creation with valid data."""
        # Providing both name and category for Magazine creation
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_magazine_creation_invalid(self):
        """Test Magazine creation with invalid data."""
        with self.assertRaises(ValueError):
            # Providing empty name and missing category for Magazine creation
            magazine = Magazine(1, "", "")  

if __name__ == "__main__":
    unittest.main()
