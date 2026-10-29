from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    con = sqlite3.connect("cricket.db")
    con.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            team TEXT,
            runs INTEGER
        )
    """)
    con.commit()
    return con

@app.route("/")
def home():
    return "Cricket Player Management Application"

@app.route("/players")
def get_players():
    con = get_db()

    count = con.execute(
        "SELECT COUNT(*) FROM players").fetchone()[0]

    if count == 0:
        con.execute(
            "INSERT INTO players (name, team, runs) VALUES (?, ?, ?)",
            ("Virat Kohli", "India", 85)
        )
        con.execute(
            "INSERT INTO players (name, team, runs) VALUES (?, ?, ?)",
            ("Rohit Sharma", "India", 72)
        )
        con.commit()

    rows = con.execute(
        "SELECT * FROM players"
    ).fetchall()

    con.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
