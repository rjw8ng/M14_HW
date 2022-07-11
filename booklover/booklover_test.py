import unittest
from booklover import Booklover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`. 
        book = Booklover("Royal", "rjw8ng", "mystery")
        book.add_book('Test', 3)
        
        self.assertTrue('Test' in book.book_list.values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book = Booklover("Royal", "rjw8ng", "mystery")
        book.add_book('Test2', 3)
        book.add_book('Test2', 3)
        
        expected = 1
        
        self.assertEqual(len(book.book_list), expected)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book = Booklover("Royal", "rjw8ng", "mystery")
        book.add_book('Test3', 3)
        self.assertTrue(book.has_read('Test3'))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book = Booklover("Royal", "rjw8ng", "mystery")
        book.add_book('Test3', 3)
        self.assertFalse(book.has_read("Does Not Exist"))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book = Booklover("Royal", "rjw8ng", "mystery")
        book.add_book('Book1', 1)
        book.add_book('Book2', 2)
        book.add_book('Book3', 3)

        expected = 3
        
        self.assertTrue(book.num_books_read, expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book = Booklover("Royal", "rjw8ng", "mystery")
        book.add_book('Book1', 4)
        book.add_book('Book2', 1)
        book.add_book('Book3', 4)
        
        x = True
        for i in book.fav_books()["book_rating"]:
            if i > 3:
                pass
            else:
                x = False
        
        self.assertTrue(x)


if __name__ == '__main__':

    unittest.main(verbosity=3)