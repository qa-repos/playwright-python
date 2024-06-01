from playwright.sync_api import APIRequestContext

from lib.serializers.models.all_books_modal import AllBooksModal


class BookstoreHelper:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

        self.get_books_url = '/BookStore/v1/Books'

    def get_books(self):
        response = self.request.get(self.get_books_url)
        books = response.json()

        AllBooksModal.model_validate(books)

        return books
