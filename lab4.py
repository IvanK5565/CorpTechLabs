import pprint
import json

class Library:
    def __init__(self):
        self.books = {}

    def addBook(self, num, info):
        self.books[num] = info

    def deleteBook(self, num):
        if num in self.books:
            del self.books[num]
        else:
            print("Книга з таким номером не знайдена.")

    def find(self, key, attr):
        res = {num: book for num, book in self.books.items() if book[attr] == key}
        return res

    def getBook(self, num):
        return self.books.get(num, "Книга з таким номером не знайдена.")

    def saveToFile(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)
        print(f"Інформацію збережено у файл {filename}")

    def loadFromFile(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.books = json.load(file)
            print(f"Інформацію завантажено з файлу {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")
        except json.JSONDecodeError:
            print(f"Помилка при читанні файлу {filename}.")

lib = Library()

lib.addBook(1, {'автор': 'Тарас Шевченко', 'назва': 'Кобзар', 'видавництво': 'Знання', 'жанр': 'Поезія', 'рік видання': 1840})
lib.addBook(2, {'автор': 'Іван Франко', 'назва': 'Захар Беркут', 'видавництво': 'Дніпро', 'жанр': 'Проза', 'рік видання': 1883})
lib.addBook(3, {'автор': 'Леся Українка', 'назва': 'Лісова пісня', 'видавництво': 'Київ', 'жанр': 'Драма', 'рік видання': 1911})

print(f"Книги автора 'Тарас Шевченко':")
pprint.pp(lib.find('Тарас Шевченко', 'автор'))
print("Книги, видані в 1883 році:")
pprint.pp(lib.find(1883, 'рік видання'))
print("Книги жанру 'Поезія':")
pprint.pp(lib.find('Поезія', 'жанр'))

print("Інформація про книгу 2:", )
pprint.pp(lib.getBook(2))

lib.deleteBook(1)
print("Книги після видалення 1:")
pprint.pp(lib.books)


lib.saveToFile("data")
lib2 = Library()
lib2.loadFromFile("data")
pprint.pp(lib2.books)
