from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route("/")
def introduce_myself():
    return '2021113438 전자공학부 안영석.'


@app.route('/me/')
def pertainable_to_me():
    return render_template('index.html', my_img='경북대학교.jpeg')


if __name__ == "__main__":
    app.run(debug=True)
