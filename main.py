# by Lydia Vasilyeva
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    print("123")
    return render_template("home.html")

@app.route("/lydia")
def lydia():
    return "Hello, Lydia"

@app.route("/about")
def about():
    print()
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
