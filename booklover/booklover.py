import pandas as pd
import numpy as np
import unittest

class Booklover:
    
    def __init__(self, name, email, fav_genre, num_books= 0, book_list= pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name'].values:
            return "Book already in list"
        else:
            new_book = pd.DataFrame({
                        'book_name': [book_name], 
                        'book_rating': [book_rating]
                        })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        if book_name in self.book_list.values:
            return True
        else:
            return False
    
    def num_books_read(self):
        return int(self.book_list["book_name"].count())
    
    def fav_books(self):
        return self.book_list[self.book_list["book_rating"] > 3]
