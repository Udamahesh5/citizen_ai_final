from flask import Flask, request, jsonify, render_template
from utils import analyze_sentiment, granite_generate
import datetime, sqlite3, os

app = Flask(__name__)
DB = "citizen.db"

# ---------- helpers ---------- #
def init_db():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS feedback(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        text TEXT,
                        sentiment TEXT,
                        created TIMESTAMP)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS messages(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        role TEXT,
                        content TEXT,
                        created TIMESTAMP)""")

init_db()

# ---------- routes ---------- #
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dash():
    return render_template("dashboard.html")

# Real‑time Chat
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO messages(role,content,created) VALUES (?,?,?)",
                    ("user", user_msg, datetime.datetime.utcnow()))
    bot_reply = granite_generate(user_msg)
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO messages(role,content,created) VALUES (?,?,?)",
                    ("bot", bot_reply, datetime.datetime.utcnow()))
    return jsonify({"response": bot_reply})

# Feedback + sentiment
@app.route("/feedback", methods=["POST"])
def feedback():
    fb_text = request.json.get("text", "")
    sentiment = analyze_sentiment(fb_text)
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO feedback(text,sentiment,created) VALUES (?,?,?)",
                    (fb_text, sentiment, datetime.datetime.utcnow()))
    return jsonify({"sentiment": sentiment})

# Dashboard data
@app.route("/dashboard-data")
def dash_data():
    with sqlite3.connect(DB) as con:
        rows = con.execute("SELECT sentiment, COUNT(*) FROM feedback GROUP BY sentiment").fetchall()
    return jsonify({sent or "Unknown": cnt for sent, cnt in rows})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
