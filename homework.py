#Завдання 1Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об’єм двигуна, колір машини, ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price
    def display_info(self):
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume}")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price}")

    def update_price(self, new_price):
        self.price = new_price
car1 = Car("Toyota Camry", 2020, "Toyota", 2.0, "Синій", 25000)
car1.display_info()
#Завдання 2Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Book:
    def __init__(self, title, publication_year, publisher, genre, author, price):
        self.title = title
        self.publication_year = publication_year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Назва книги: {self.title}")
        print(f"Рік видання: {self.publication_year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price}")

    def update_price(self, new_price):
        self.price = new_price
book1 = Book("Гаррі Поттер і філософський камінь", 1997, "Bloomsbury", "Фентезі", "Дж. К. Роулінг", 20)
book1.display_info()
#Завдання 3Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
stadium1 = Stadium("Олімпійський стадіон", "1980-07-17", "Україна", "Київ", 70000)
stadium1.display_info()
