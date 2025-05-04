from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("./lessons/arb_read.json", "r") as fd:
    LESSON = json.load(fd)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        LESSON['title'] = request.form['title']
        LESSON['content'] = request.form['content']
    return render_template('lesson.html', lesson=LESSON)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

