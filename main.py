from conection import *
from table import *
from show_data import*
from show_9 import*

connection = create_connection(
    "postgres", "admin", "root", "127.0.0.1", "5432"
)

execute_query(connection, create_Guests)
execute_query(connection, create_Rooms)
execute_query(connection, create_GuestRegistrations)

cur = connection.cursor()

# create(cur)
# show(cur)
tables = ['Guests', 'Rooms', 'GuestRegistrations']

for table in tables:
    print(f"\nTable: {table}")
    fetch_table_data(cur, table)