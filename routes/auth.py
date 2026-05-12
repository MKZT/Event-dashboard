# auth.py

import hashlib
import jwt
import datetime
from functools import wraps
from flask import request, jsonify

# =========================
# SECRET KEY
# =========================

SECRET_KEY = "dev_secret_key"


# =========================
# PASSWORD HASHING
# =========================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed):
    return hashlib.sha256(password.encode()).hexdigest() == hashed


# =========================
# JWT TOKEN GENERATION
# =========================

def generate_token(user_id, role):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(hours=24),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# =========================
# TOKEN REQUIRED DECORATOR
# =========================

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            data = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"],
            )

            request.user = data

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401

        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated


# =========================
# ROLE CHECK DECORATOR
# =========================

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = getattr(request, "user", None)

            if not user or user.get("role") != role:
                return jsonify(
                    {"error": "Access denied"}
                ), 403

            return f(*args, **kwargs)

        return decorated

    return wrapper