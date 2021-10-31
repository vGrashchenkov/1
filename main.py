from csv import DictReader
from json import load, dump

BOOKS_FILE = 'data/books.csv'
USERS_FILE = 'data/users.json'
REFERENCE_FILE = 'result.json'


def books_read(file_path):
    with open(file_path) as csv:
        reader = DictReader(f=csv, fieldnames=["title", "author", "genre", "pages"], restkey='trash')
        results = list()
        for row in reader:
            row.pop('trash')
            results.append(row)
    results.pop(0)
    return results


def users_read(file_path):
    with open(file_path) as json:
        reader = load(fp=json, object_hook=filtered_user)
        results = list()
        for row in reader:
            results.append(row)

    return results


def filtered_user(user_dict):
    new_user = user_dict.copy()

    for key in user_dict:
        if key.lower() not in ["name", "gender", "address", "age"]:
            new_user.pop(key)

    return new_user


def slice_books(books_list, users_count):
    books_size = len(books_list)
    slice_size = books_size // users_count
    remain = books_size % users_count
    result = []
    iterator = iter(books_list)

    for i in range(users_count):
        result.append(dict(books=[]))

        for j in range(slice_size):
            result[i].get('books').append(next(iterator))

        if remain:
            result[i].get('books').append(next(iterator))
            remain -= 1

    return result


def reference(users_list, books_list):
    result = []

    for user, book in zip(users_list, books_list):
        user.update(book)
        result.append(user)

    return result


if __name__ == '__main__':
    books = books_read(BOOKS_FILE)
    users = users_read(USERS_FILE)

    with open(REFERENCE_FILE, 'w') as file:
        data = reference(users, slice_books(books, len(users)))
        dump(fp=file, obj=data, ensure_ascii=False, indent=4)
