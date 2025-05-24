import os
class Config:
    MONGO_URI = "mongodb+srv://admin:admin@cluster0.pojhz.mongodb.net/cinema?retryWrites=true&w=majority"
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")  