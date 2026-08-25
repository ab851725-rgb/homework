import sqlite3

def create_tables(connection): 
    # connection.execute("DROP TABLE IF EXISTS students")
    connection.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')

def insert_books(connection, name, author, publication_year, genre, number_of_pages, number_of_copies):
    connection.execute('''
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, author, publication_year, genre, number_of_pages, number_of_copies))
    connection.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.sqlite3')
    create_tables(conn)
    insert_books(conn, "Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 480, 5)
    insert_books(conn, "1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 3)
    insert_books(conn, "Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 672, 4)
    insert_books(conn, "Властелин Колец", "Джон Р. Р. Толкин", 1954, "Фэнтези", 1050, 2)
    insert_books(conn, "Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", 399, 10)
    insert_books(conn, "Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 7)
    insert_books(conn, "Алхимик", "Пауло Коэльо", 1988, "Приключения", 224, 6)
    insert_books(conn, "Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 416, 4)
    insert_books(conn, "Шерлок Холмс", "Артур Конан Дойл", 1887, "Детектив", 300, 8)
    insert_books(conn, "Марсианин", "Энди Уир", 2011, "Фантастика", 369, 3)
    conn.close()