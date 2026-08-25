import sqlite3

def create_tables(connection): 
    connection.execute("DROP TABLE IF EXISTS students")
    # делаем SQL запрос для создания таблицы
    connection.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

def get_all_students(connection):
    result = connection.execute("SELECT * FROM students")
    return result.fetchall()

def get_student_by_name(connection, name):
    result = connection.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )

def change_age(connection, student_id, new_age):
    connection.execute(
        '''UPDATE status SET age = ? WHERE id = ?''',
        (new_age, student_id)
    )
    connection.commit()

# def get_student_by_id(connection, name):
#     return = connection

# def dell_student(connection)
 
if __name__ == '__main__':
    conn = sqlite3.connect('database.sqlite3')
    create_tables(conn)
    add_student(conn, 'Igor', 30, 'Bishkek')
    add_student(conn, 'Jeka', 22, 'Ingush')
    add_student(conn, 'purple.Muslie', 228, 'Ganjubasik')
    print(get_all_students(conn,))
