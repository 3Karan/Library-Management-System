from app import create_app
from app.database import init_db

app = create_app()

# Initialize the database when the app starts (or manually run the script once)
init_db()

if __name__ == "__main__":
    app.run(debug=True)
