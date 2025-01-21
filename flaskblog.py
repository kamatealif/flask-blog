from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    name = "alif"
    return f"<h1>Hello {name}!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ =="__main__":
    app.run(debug=True)