import csv
import json

from otus_course.hw4 import CSV_FILE
from otus_course.hw4 import JSON_FILE


def load_data():
    with open(CSV_FILE, newline='') as books:
        books_read = csv.DictReader(books)
        books_data = list(books_read)

    with open(JSON_FILE) as users:
        users_data = json.load(users)

    return books_data, users_data


def distribute_books(books, users):
    result = []

    total_books = len(books)
    total_users = len(users)

    books_per_user = total_books // total_users
    remaining_books = total_books % total_users

    book_index = 0

    for user in users:
        user_books = []

        for _ in range(books_per_user):
            user_books.append(books[book_index])
            book_index = (book_index + 1) % total_books

        if remaining_books > 0:
            user_books.append(books[book_index])
            book_index = (book_index + 1) % total_books
            remaining_books -= 1

        result.append({
            "user": user,
            "books": user_books
        })

    return result


def save_result(result):
    with open('result.json', 'w') as result_file:
        json.dump(result, result_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    books_data, users_data = load_data()
    result_data = distribute_books(books_data, users_data)
    save_result(result_data)
