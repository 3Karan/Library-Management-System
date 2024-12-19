from flask import Blueprint, request, jsonify
from .models import add_book, get_books, get_book_by_id, update_book, delete_book
from .auth import token_required, generate_jwt_token  # Assuming token_required decorator handles token verification

book_bp = Blueprint('books', __name__)

# login route to generate the JWT token
@book_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == 'admin' and password == 'password':
        token = generate_jwt_token('admin')  # Generate the token
        print(f"Generated Token: {token}")  # Log the token for debugging
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# Create a new book
@book_bp.route('/', methods=['POST'])
@token_required  # Ensuring only authenticated users can add books
def create_book():
    data = request.get_json()

    # Ensure that the required data is provided
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')
    genre = data.get('genre')

    if not title or not author or not year or not genre:
        return jsonify({"message": "Missing required fields"}), 400
    
    # Add the book to the database
    add_book(title, author, year, genre)
    return jsonify({"message": "Book added successfully"}), 201

# Get all books with pagination and optional search query
@book_bp.route('/', methods=['GET'])
def get_all_books():
    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Search query (optional)
    search = request.args.get('search', '', type=str)
    
    # Get books from the database, passing pagination and search query
    books = get_books(page, per_page, search)
    
    # Return books as a list of dictionaries
    return jsonify([dict(book) for book in books])

# Get a single book by its ID
@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Fetch the book by ID from the database
    book = get_book_by_id(book_id)
    if book:
        return jsonify(dict(book))  # Return the book as JSON
    return jsonify({"message": "Book not found"}), 404

# Update a book's information by ID
@book_bp.route('/<int:book_id>', methods=['PUT'])
@token_required  # Ensuring only authenticated users can update books
def update_book_route(book_id):
    data = request.get_json()

    # Ensure that the required data is provided
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')
    genre = data.get('genre')

    if not title or not author or not year or not genre:
        return jsonify({"message": "Missing required fields"}), 400
    
    # Update the book in the database
    update_book(book_id, title, author, year, genre)
    return jsonify({"message": "Book updated successfully"}), 200

# Delete a book by its ID
@book_bp.route('/<int:book_id>', methods=['DELETE'])
@token_required  # Ensuring only authenticated users can delete books
def delete_book_route(book_id):
    # Delete the book from the database
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 200
