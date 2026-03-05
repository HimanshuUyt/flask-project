from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

db = client["student_db"]
collection = db["students"]


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():

    try:
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")

        data = {
            "name": name,
            "age": age,
            "email": email
        }

        collection.insert_one(data)

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=str(e))


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)