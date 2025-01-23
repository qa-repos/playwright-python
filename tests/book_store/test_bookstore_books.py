import time
import pytest
import uuid

from conftest import request_context
from lib.helpers import BookstoreHelper, UserHelper


class TestBookStore:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request_context) -> None:
        self.bookstore_helper = BookstoreHelper(request_context)
        self.user_helper = UserHelper()
        self.username = f"{int(time.time())}"
        self.password = "P@ssw0rd"

    @pytest.mark.api
    def test_get_all_books(self, request_context) -> None:
        books = self.bookstore_helper.get_books()
        print(books)
        assert len(books) > 0

    @pytest.mark.api
    def test_register_new_user(self, request_context) -> None:
        new_user = self.user_helper.register_new_user(request_context, self.username, self.password)
        user_id = new_user['userID']
        assert str(uuid.UUID(user_id, version=4)) == user_id
        assert new_user['username'] == self.username

    @pytest.mark.api
    def test_login_successfully(self, request_context) -> None:
        self.user_helper.login_to_bookstore(request_context, self.username, self.password)

