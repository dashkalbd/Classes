from datetime import date


class Person:
    def __init__(self, full_name="", birth_date=None, phone="",
                 city="", country="", address=""):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        self.full_name = input("ПІБ: ")
        self.phone = input("Телефон: ")
        self.city = input("Місто: ")
        self.country = input("Країна: ")
        self.address = input("Домашня адреса: ")

        day = int(input("День народження (1-31): "))
        month = int(input("Місяць народження (1-12): "))
        year = int(input("Рік народження (напр. 1990): "))
        self.birth_date = date(year, month, day)

    def display(self):
        print("ПІБ:", self.full_name)
        print("Дата народження:", self.birth_date.strftime("%d.%m.%Y"))
        print("Вік:", self.get_age())
        print("Телефон:", self.phone)
        print("Місто:", self.city)
        print("Країна:", self.country)
        print("Адреса:", self.address)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age = age - 1

        return age

    def change_address(self, new_city, new_country, new_address):
        self.city = new_city
        self.country = new_country
        self.address = new_address


p = Person()
p.input_data()

print()
p.display()

print()
print("Після переїзду:")
p.change_address("Львів", "Україна", "пл. Ринок, 5")
p.display()