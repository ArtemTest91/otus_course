import csv
import json
from otus_course.hw4 import CSV_FILE, JSON_FILE


def read_books_from_csv():
    try:
        with open(CSV_FILE, newline='') as books_file:
            books_reader = csv.DictReader(books_file)
            return list(books_reader)
    except FileNotFoundError:
        print(f"Ошибка: Файл {CSV_FILE} не найден.")
        return []


def read_users_from_json():
    try:
        with open(JSON_FILE) as users_file:
            return json.load(users_file)
    except FileNotFoundError:
        print(f"Ошибка: Файл {JSON_FILE} не найден.")
        return []


def load_data():
    books = read_books_from_csv()
    users = read_users_from_json()

    for book in books:
        if 'Pages' in book:
            book['pages'] = int(book.pop('Pages'))

    return books, users


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
                "title": books[book_index].get("Title", ""),
                "author": books[book_index].get("Author", ""),
                "pages": books[book_index].get("pages", 0),
                "genre": books[book_index].get("Genre", "")
            })

            book_index += 1

        if remaining_books > 0:
            user_books.append({
                "title": books[book_index].get("Title", ""),
                "author": books[book_index].get("Author", ""),
                "pages": books[book_index].get("pages", 0),
                "genre": books[book_index].get("Genre", "")
            })

            book_index += 1
            remaining_books -= 1

        result.append({
            "name": user.get("name", ""),
            "gender": user.get("gender", ""),
            "address": user.get("address", ""),
            "age": user.get("age", 0),
            "books": user_books
        })

    return result


def save_result(result):
    with open('result.json', 'w') as result_file:
        json.dump(result, result_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    books, users = load_data()
    if not books or not users:
        print("Ошибка при загрузке данных. Пожалуйста, проверьте наличие файлов.")
    else:
        result_data = distribute_books(books, users)
        save_result(result_data)

