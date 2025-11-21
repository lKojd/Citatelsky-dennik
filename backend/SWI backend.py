from flask import Flask
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_message_from_db():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="prototyp"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT message FROM test LIMIT 1")
    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return row[0] if row else "Žiadna správa v databáze."

@app.route("/hello")
def hello():
    return "Hello from Python server!"

@app.route("/db")
def db_message():
    return f"Správa z databázy: {get_message_from_db()}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
