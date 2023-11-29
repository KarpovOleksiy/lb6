from tabulate import tabulate

def show(cur):
    # Запит 1: Відобразити всі номери в яких є телевізор
    cur.execute("SELECT room_number FROM Rooms WHERE has_tv = TRUE")
    result_1 = cur.fetchall()
    print("Номери з телевізором:")
    print(tabulate(result_1, headers=["Room Number"]))

    # Запит 2: Порахувати кінцеву дату проживання в готелі для кожного гостя
    cur.execute("""
        SELECT guest_id, check_in_date + duration AS end_stay_date
        FROM GuestRegistrations
    """)
    result_2 = cur.fetchall()
    print("Кінцеві дати проживання для кожного гостя:")
    print(tabulate(result_2, headers=["Guest ID", "End Stay Date"]))

    # Запит 3: Порахувати кількість номерів кожної категорії в готелі
    cur.execute("""
        SELECT category, COUNT(*) AS count
        FROM Rooms
        GROUP BY category
    """)
    result_3 = cur.fetchall()
    print("Кількість номерів кожної категорії:")
    print(tabulate(result_3, headers=["Category", "Count"]))

    # Запит 4: Порахувати повну вартість проживання для кожного гостя
    cur.execute("""
        SELECT guest_id, SUM(price_per_night * duration) AS total_cost
        FROM GuestRegistrations
        JOIN Rooms ON GuestRegistrations.room_number = Rooms.room_number
        GROUP BY guest_id
    """)
    result_4 = cur.fetchall()
    print("Повна вартість проживання для кожного гостя:")
    print(tabulate(result_4, headers=["Guest ID", "Total Cost"]))

    # Запит 5: Порахувати кількість номерів кожної категорії на кожному поверсі
    cur.execute("""
        SELECT floor, category, COUNT(*) AS count
        FROM Rooms
        GROUP BY floor, category
    """)
    result_5 = cur.fetchall()
    print("Кількість номерів кожної категорії на кожному поверсі:")
    print(tabulate(result_5, headers=["Floor", "Category", "Count"]))

    # Запит 6: Відобразити всіх гостей, які проживають(або проживали) в номерах обраної категорії
    category_to_search = 'Standard'
    cur.execute("""
        SELECT Guests.*
        FROM Guests
        JOIN GuestRegistrations ON Guests.registration_number = GuestRegistrations.guest_id
        JOIN Rooms ON GuestRegistrations.room_number = Rooms.room_number
        WHERE Rooms.category = %s
    """, (category_to_search,))
    result_6 = cur.fetchall()
    print("Гості в номерах обраної категорії:", category_to_search)
    print(tabulate(result_6, headers=["Registration Number", "Last Name", "First Name", "Middle Name", "City"]))