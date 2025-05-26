import jwt
import datetime

SECRET_KEY = "supetsecret"


# Пользователь, которого мы "аутентифицировали"
user_data = {
    "user_id": 123,
    "username": "test_user"
}


def create_jwt(data):
    payload = {
        "user": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        "iat": datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return "❌ Token expired"
    except jwt.InvalidTokenError:
        return "❌ Invalid token"




if __name__ == "__main__":
    token = create_jwt(user_data)
    print("✅ JWT Token:\n", token)

    decoded = verify_jwt(token)
    print("\n🔍 Decoded Payload:\n", decoded)