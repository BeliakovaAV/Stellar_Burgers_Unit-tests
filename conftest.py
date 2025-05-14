import pytest

from bun import Bun


@pytest.fixture
def wholegrain_bun():
    return Bun("Цельнозерновая", 1.54)



# @pytest.fixture
# def book_with_1_favorite_book(book):
#   book.add_new_book('Сияние')
#  book.add_book_in_favorites('Сияние')
# return book
