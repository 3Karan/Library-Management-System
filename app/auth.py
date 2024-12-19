from functools import wraps
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta

# Simulated token-based authentication
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for 'Authorization' header with simulated token for testing
        token = request.headers.get('Authorization')
        if not token or token != 'Bearer valid_token':
            return jsonify({'message': 'Token is missing or invalid'}), 403
        return f(*args, **kwargs)
    return decorated_function

# JWT Authentication
SECRET_KEY = "secret"  # Use a secret key for JWT token encoding/decoding

def token_required_jwt(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
            
        print("Token received:", token)  # Add this line to print the token in the logs

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            # Decode the token using the secret key
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user']  # Extract user info from token
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(current_user, *args, **kwargs)
    return decorated_function



def generate_jwt_token(user_id):
    expiration_time = datetime.utcnow() + timedelta(minutes=5)  # Set a shorter expiration for testing
    payload = {
        'user': user_id,
        'exp': expiration_time
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
