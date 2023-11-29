import psycopg2
from psycopg2 import sql
from tabulate import tabulate

def fetch_table_data(cur, table):
    # Вивід структури таблиці
    structure_query = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table}';"
    cur.execute(structure_query)
    structure_data = cur.fetchall()
    
    # Вивід заголовків стовпців
    columns = [desc[0] for desc in structure_data]
    print(f"\nStructure of Table: {table}")
    print(tabulate(structure_data, headers=['Column Name', 'Data Type'], tablefmt="pretty"))

    # Вивід даних таблиці
    data_query = f"SELECT * FROM {table};"
    cur.execute(data_query)
    data = cur.fetchall()
    print(f"\nData of Table: {table}")
    print(tabulate(data, headers=columns, tablefmt="pretty"))