from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['DATABASE'] = 'library.db'  # SQLite database for simplicity
    app.config['DEBUG'] = True

        
    from .routes import book_bp  # Remove the import for member_bp
    app.register_blueprint(book_bp, url_prefix='/books')
    

    
    return app
