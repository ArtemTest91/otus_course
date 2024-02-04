import csv
import json

from otus_course.hw4 import CSV_FILE
from otus_course.hw4 import JSON_FILE

def read_books_from_csv():
    with open(CSV_FILE, newline='') as books:
        books_read = csv.DictReader(books)
        books_data = list(books_read)

    return books_data


def read_users_from_json():
    with open(JSON_FILE) as users:
        users_data = json.load(users)

    return users_data


def load_data():
    books_data = read_books_from_csv()
    users_data = read_users_from_json()

    for book in books_data:
        book['pages'] = int(book['Pages'])
        del book['Pages']

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
            user_books.append({
                "title": books[book_index]["Title"],
                "author": books[book_index]["Author"],
                "pages": books[book_index]["pages"],
                "genre": books[book_index]["Genre"]
            })
            book_index = (book_index + 1) % total_books

        if remaining_books > 0:
            user_books.append({
                "title": books[book_index]["Title"],
                "author": books[book_index]["Author"],
                "pages": books[book_index]["pages"],
                "genre": books[book_index]["Genre"]
            })
            book_index = (book_index + 1) % total_books
            remaining_books -= 1

        result.append({
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
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
