from flask import Flask, request, render_template
from database import add_word, get_word, view_words, update_word, delete_word
import os


app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])

def add():
    word = request.form['word']
    meaning = request.form['meaning']
    example = request.form['example']

    result = add_word(word, meaning, example)
    
    if result:
        return render_template("index.html", message="The word already exists!")
    else:
        return render_template("index.html", message="The word is added!")

@app.route('/search', methods=['POST'])

def search():
    word = request.form['word']
    result = get_word(word)
    return render_template('search.html', word=result)

@app.route('/view')

def view():
    words = view_words()
    return render_template('view.html', words=words)


@app.route('/update', methods=['POST'])

def update():
    word = request.form['word']
    meaning = request.form['meaning']
    example = request.form['example']

    update_word(word, meaning, example)
    return render_template("index.html", message="The word's meaning and example are updated!")

@app.route('/delete', methods=['POST'])

def delete():
    word = request.form['word']
    result = delete_word(word)
    
    if result:
        return render_template("index.html", message="The word is deleted!")
    else:
        return render_template("index.html", message="The word does not exist!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)