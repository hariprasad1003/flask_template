from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)