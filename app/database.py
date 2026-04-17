import mysql.connector
import os

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "Marcelo@123"),
        database=os.getenv("DB_NAME", "cashback_db")
    )