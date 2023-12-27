import time
import pytest
from conftest import request_context
from lib.helpers import BookstoreHelper, UserHelper


class TestBookStore:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request_context) -> None:
        self.bookstore_helper = BookstoreHelper(request_context)
        self.user_helper = UserHelper()
        self.username = f"{int(time.time())}"
        self.password = "P@SSWord1"

    @pytest.mark.api
    def test_get_all_books(self, request_context) -> None:
        books = self.bookstore_helper.get_books()
        assert books.ok, "Failed to get all books!"
        books_response = books.json()
        assert books_response, "No books found!"

    def test_register_new_user(self, request_context) -> None:
        self.user_helper.register_new_user(request_context, self.username, self.password)

    def test_login_successfully(self, request_context) -> None:
        self.user_helper.login_to_bookstore(request_context, self.username, self.password)

