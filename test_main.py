import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):

    @patch('builtins.input', return_value='Harry Potter')
    def test_get_search_item(self, mock_input):
        result = main.get_search_item()
        self.assertEqual(result, "Harry Potter")


    def test_get_params(self):
        d1 = main.get_params('Harry Potter')
        d2 = {
        "q": 'Harry Potter',
        "orderBy": "relevance",
        "maxResults": 5,
    }
        self.assertDictEqual(d1, d2)

    @patch('builtins.input', return_value='3')
    def test_get_user_selection(self, mock_input):
        result = main.get_user_selection()
        self.assertEqual(result, "3")

    def test_get_book_choices(self):
        lst = main.get_book_list(main.get_params('Harry Potter'))
        d1 = main.get_book_choices(lst)
        d2 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
        self.assertTrue(d1.keys() == d2.keys())

    def test_get_author_with_author(self):
        lst = main.get_book_list(main.get_params('Harry Potter'))
        book = lst[0]
        author = main.get_author(book)
        self.assertIsNotNone(author)

    def test_get_author_without_author(self):
        lst = main.get_book_list(main.get_params('The Bible'))
        book = lst[0]
        author = main.get_author(book)
        self.assertIsNotNone(author)

    def test_get_publisher_with_publisher(self):
        lst = main.get_book_list(main.get_params('To Kill a Mockingbird'))
        book = lst[0]
        publisher = main.get_publisher(book)
        self.assertIsNotNone(publisher)

    def test_get_publisher_without_publisher(self):
        lst = main.get_book_list(main.get_params('The Bible'))
        book = lst[0]
        publisher = main.get_publisher(book)
        self.assertIsNotNone(publisher)

    def test_get_title(self):
        lst = main.get_book_list(main.get_params('To Kill a Mockingbird'))
        book = lst[0]
        title = main.get_title(book)
        self.assertIsNotNone(title)

if __name__ == '__main__':
    unittest.main()
