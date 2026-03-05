from flask import Flask, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("your_mongodb_connection_string")
db = client.todoDB
collection = db.todoItems


@app.route("/submittodoitem", methods=["POST"])
def submitTodo():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    data = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(data)

    return "Item Added Successfully"

@app.route("/todo")
def todo():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)