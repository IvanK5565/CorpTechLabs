import pprint

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

biblioteka = Library()

biblioteka.addBook(1, {'автор': 'Тарас Шевченко', 'назва': 'Кобзар', 'видавництво': 'Знання', 'жанр': 'Поезія', 'рік видання': 1840})
biblioteka.addBook(2, {'автор': 'Іван Франко', 'назва': 'Захар Беркут', 'видавництво': 'Дніпро', 'жанр': 'Проза', 'рік видання': 1883})
biblioteka.addBook(3, {'автор': 'Леся Українка', 'назва': 'Лісова пісня', 'видавництво': 'Київ', 'жанр': 'Драма', 'рік видання': 1911})

print(f"Книги автора 'Тарас Шевченко':")
pprint.pp(biblioteka.find('Тарас Шевченко', 'автор'))
print("Книги, видані в 1883 році:")
pprint.pp(biblioteka.find(1883, 'рік видання'))
print("Книги жанру 'Поезія':")
pprint.pp(biblioteka.find('Поезія', 'жанр'))

print("Інформація про книгу 2:", )
pprint.pp(biblioteka.getBook(2))

biblioteka.deleteBook(1)
print("Книги після видалення 1:")
pprint.pp(biblioteka.books)


