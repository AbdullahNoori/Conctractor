from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')

client = MongoClient(host=f'{host}?retryWrites=false')
db = client.Store
sneakers = db.sneakers

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('home.html', sneakers=sneakers.find())

@app.route("/sneakers/new")
def sneakers_new():
    # create new sneaker to sell
    return render_template("sneakers_new.html")

@app.route('/sneakers', methods=['POST'])
def sneaker_upload():
    # upload new sneaker
    sneaker = {
        "title": request.form.get("title"),
        "image": request.form.get("image"),
        "price": request.form.get("price"),
    }
    sneaker_id = sneakers.insert_one(sneaker).inserted_id
    return redirect(url_for("sneaker_show", sneaker_id=sneaker_id))

@app.route("/sneakers/<sneaker_id>")
def sneaker_show(sneaker_id):
    # show sneaker information
    sneaker = sneakers.find_one({"_id": ObjectId(sneaker_id)})
    return render_template("sneaker_show.html", sneaker=sneaker)

@app.route("/sneakers/<sneaker_id>/edit")
def sneaker_edit(sneaker_id):
    # show edit form
    sneaker = sneakers.find_one({"_id" : ObjectId(sneaker_id)})
    return render_template("sneaker_edit.html", sneaker=sneaker)

@app.route("/sneakers/<sneaker_id>", methods=["POST"])
def sneaker_update(sneaker_id):
    updated_sneaker = {
        "title": request.form.get("title"),
        "image": request.form.get("image"),
        "price": request.form.get("price"),
    }
    sneakers.update_one({"_id": ObjectId(sneaker_id)},{ "$set": updated_sneaker})
    return redirect(url_for("sneaker_show", sneaker_id=sneaker_id))

@app.route("/sneaker/<sneaker_id>/delete", methods=["POST"])
def sneaker_delete(sneaker_id):
    sneakers.delete_one({"_id": ObjectId(sneaker_id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))