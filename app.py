from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import random

app = Flask(__name__)
client = MongoClient('mongodb://admin:password@mongo:27017/')
db = client['marvel_entries']

@app.route('/')
def index():
    print("Starting localhost")
    return render_template('index.html', title='Welcome to Marvel World')

@app.route('/new_entry', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'POST':
        name = request.form['name']
        character = request.form['character']
        color = random_color()
        entry = {'name': name, 'character': character, 'color': color}
        db.entries.insert_one(entry)
        return redirect('/view_entries')
    return render_template('new_entry.html')

@app.route('/view_entries')
def view_entries():
    entries = db.entries.find()
    return render_template('view_entries.html', entries=entries)

def random_color():
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    return random.choice(colors)

if __name__ == '__main__':
    app.run()
