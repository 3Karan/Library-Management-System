from .database import get_db

def add_book(title: str, author: str, year: int, genre: str):
    db = get_db()
    db.execute('INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)', 
               (title, author, year, genre))
    db.commit()

def get_books(page: int, per_page: int, search: str = ''):
    db = get_db()
    query = f"SELECT * FROM books WHERE title LIKE ? OR author LIKE ? LIMIT ? OFFSET ?"
    books = db.execute(query, (f"%{search}%", f"%{search}%", per_page, (page - 1) * per_page)).fetchall()
    return books

def get_book_by_id(book_id: int):
    db = get_db()
    book = db.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    return book

def update_book(book_id: int, title: str, author: str, year: int, genre: str):
    db = get_db()
    db.execute('UPDATE books SET title = ?, author = ?, year = ?, genre = ? WHERE id = ?',
               (title, author, year, genre, book_id))
    db.commit()

def delete_book(book_id: int):
    db = get_db()
    db.execute('DELETE FROM books WHERE id = ?', (book_id,))
    db.commit()

# Similar functions for members can be added here as needed.
