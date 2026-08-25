import sqlite3

def create_tables(connection): 
    # делаем SQL запрос для создания таблицы
    connection.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    ''')

def add_student(connection, name, age, city):
    connection.execute('''
        INSERT INTO students (name, age, city)
        VALUES (?, ?, ?)
    ''', (name, age, city))
    connection.commit()

def dell_student(connection)

if __name__ == '__main__':
    conn = sqlite3.connect('database.sqlite3')
    create_tables(conn)
    add_student(conn, 'Igor', 30, 'Bishkek')
    add_student(conn, 'Jeka', 22, 'Ingush')