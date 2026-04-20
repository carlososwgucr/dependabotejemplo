from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/search")
def search_user():
    # SOURCE: Entrada externa controlada por el usuario
    username = request.args.get('username')

    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    # SINK: Ejecución de query donde el dato entra sin sanitizar
    # VULNERABILIDAD: SQL Injection
    query = "SELECT * FROM profiles WHERE user = '" + username + "'"
    cursor.execute(query)

    return str(cursor.fetchone())
