import random
from faker import Faker
from psycopg2 import sql

create_Guests = ("""
    CREATE TABLE IF NOT EXISTS Guests (
        registration_number INT PRIMARY KEY,
        last_name VARCHAR(50),
        first_name VARCHAR(50),
        middle_name VARCHAR(50),
        city VARCHAR(50)
    )
""")

create_Rooms = ("""
    CREATE TABLE IF NOT EXISTS Rooms (
        room_number INT PRIMARY KEY,
        floor INT,
        has_tv BOOLEAN,
        has_fridge BOOLEAN,
        capacity INT,
        category VARCHAR(20),
        price_per_night DECIMAL(8, 2)
    )
""")

create_GuestRegistrations = ("""
    CREATE TABLE IF NOT EXISTS GuestRegistrations (
        registration_code SERIAL PRIMARY KEY,
        guest_id INT,
        check_in_date DATE,
        duration INT,
        room_number INT REFERENCES Rooms(room_number)
    )
""")
def create(cur):
    fake = Faker('uk_UA')  # Використовуємо мову "uk_UA" для генерації українських імен
    row = ['Петрович', 'Анатолійович', 'Володимирович', 'Олександрович', 'Ігорович', 'Юрійович', 'Михайлович']
    # Додавання гостей
    guests_data = [
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
        (fake.unique.random_number(), fake.last_name(), fake.first_name(), fake.random_element(row), fake.city()),
    ]

    insert_guest_query = sql.SQL("INSERT INTO Guests (registration_number, last_name, first_name, middle_name, city) VALUES {}").format(
        sql.SQL(',').join(map(sql.Literal, guests_data))
    )

    cur.execute(insert_guest_query)

    # Додавання номерів
    rooms_data = [
        (101, 1, True, False, 2, 'Standard', 100.00),
        (102, 1, True, True, 3, 'Suite', 200.00),
        (103, 2, False, False, 1, 'Economy', 80.00),
        (104, 2, True, True, 4, 'Deluxe', 150.00),
        (105, 3, False, False, 1, 'Economy', 75.00),
        (106, 3, True, False, 3, 'Suite', 180.00),
        (107, 3, True, True, 5, 'Luxury', 250.00),
        (108, 1, False, True, 2, 'Standard', 120.00),
        (109, 2, True, False, 3, 'Deluxe', 160.00),
        (110, 3, False, True, 4, 'Luxury', 220.00),
    ]

    insert_room_query = sql.SQL("INSERT INTO Rooms (room_number, floor, has_tv, has_fridge, capacity, category, price_per_night) VALUES {}").format(
        sql.SQL(',').join(map(sql.Literal, rooms_data))
    )

    cur.execute(insert_room_query)

    # Додавання реєстрацій гостей
    registrations_data = [
        (fake.unique.random_number(), 1, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 2, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 3, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 4, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 5, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 6, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 7, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 1, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 3, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
        (fake.unique.random_number(), 5, fake.date_this_decade(), fake.random_int(1, 10), fake.random_int(101, 110)),
    ]

    insert_registration_query = sql.SQL("INSERT INTO GuestRegistrations (registration_code, guest_id, check_in_date, duration, room_number) VALUES {}").format(
        sql.SQL(',').join(map(sql.Literal, registrations_data))
    )

    cur.execute(insert_registration_query)