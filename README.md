
# Library Management System API

This is a RESTful API for a Library Management System built using Flask. The system allows for CRUD operations on books and members, as well as optional features such as search functionality, pagination, and token-based authentication. The API is backed by an SQLite database.

## Features
1. **CRUD Operations for Books**:
   - Create a new book
   - Retrieve a list of all books (with optional search and pagination)
   - Retrieve a single book by its ID
   - Update book details
   - Delete a book

2. **Token-based Authentication**:
   - Routes for adding, updating, and deleting books are protected by token-based authentication. 
   - A simulated token (`'Bearer valid_token'`) is required for these actions.

3. **Search and Pagination**:
   - Search books by title or author.
   - Paginate through book records using query parameters `page` and `per_page`.

## Installation

### Prerequisites
- Python 3.x
- Flask
- SQLite (used as the database)

### Steps to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. Install the required dependencies:

   ```bash
   pip install Flask pyjwt
   ```

3. Initialize the database:

   The database will be created automatically when you run the app for the first time. If needed, you can run `init_db()` manually in the `database.py` file.

4. Run the application:

   ```bash
   python run.py
   ```

5. The application will be accessible at `http://127.0.0.1:5000`.

## Endpoints

### **Books API**

#### 1. Create a New Book
   **POST** `/books/`
   - Body: 
     ```json
     {
       "title": "Book Title",
       "author": "Author Name",
       "year": 2020,
       "genre": "Fiction"
     }
     ```
   - Requires token-based authentication.

#### 2. Get All Books
   **GET** `/books/`
   - Optional Query Parameters:
     - `page`: Page number (default: 1)
     - `per_page`: Number of books per page (default: 10)
     - `search`: Search query for title or author (optional)
   - Example:
     ```bash
     curl "http://127.0.0.1:5000/books/?search=harry&page=1&per_page=5"
     ```

#### 3. Get Book by ID
   **GET** `/books/{id}`
   - Example:
     ```bash
     curl "http://127.0.0.1:5000/books/1"
     ```

#### 4. Update a Book
   **PUT** `/books/{id}`
   - Body:
     ```json
     {
       "title": "Updated Book Title",
       "author": "Updated Author",
       "year": 2021,
       "genre": "Updated Genre"
     }
     ```
   - Requires token-based authentication.

#### 5. Delete a Book
   **DELETE** `/books/{id}`
   - Requires token-based authentication.

### **Authentication**
- The API uses token-based authentication for the protected routes (Create, Update, Delete). You can use the static token `'Bearer valid_token'` for testing.

## Design Choices
- **Flask** is used to build the RESTful API.
- **SQLite** is chosen as the database for simplicity and ease of setup.
- **JWT (JSON Web Token)** is used for authentication, though a simulated token is included for simplicity in the example.
- **Blueprints** are used for modular routing, keeping routes for books and members separate (although member routes are not implemented in this version).
- **Pagination** is handled via query parameters for scalable API responses.
- **Search** allows filtering books based on title or author.

## Assumptions
- The API assumes that a user is authenticated using a static token (`'Bearer valid_token'`). This token will need to be replaced with a proper authentication mechanism for production use.
- The `library.db` database will be created automatically if it does not already exist.
- The system is designed for simplicity, so error handling is minimal and basic validation is performed.

## Limitations
- No input validation beyond required fields (e.g., no email format validation).
- Token-based authentication is implemented in a very basic manner (no user management or registration).
- Member-related routes are not yet implemented, but they can be added using a similar pattern to the book routes.
- The SQLite database is lightweight, and this system is not optimized for large-scale applications.

## License
MIT License. See the [LICENSE](LICENSE) file for details.
```

### Explanation:
1. **How to run the project**: This section outlines how to clone the repository, install dependencies, initialize the database, and run the application.
2. **Design choices**: The document explains the tools used (Flask, SQLite, JWT) and why certain architectural decisions were made (e.g., using Blueprints, pagination, and search).
3. **Assumptions and limitations**: Discusses assumptions like the use of a static token and minimal validation. It also highlights the limitations, such as the lack of user authentication and scalability considerations.

You can customize the sections according to your needs.
