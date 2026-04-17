import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Marcelo@123",
        database="cashback_db"
    )