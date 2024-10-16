from flask import Flask, render_template  # pip install flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# bitte kommentare einfügen zu neuen dingen!
