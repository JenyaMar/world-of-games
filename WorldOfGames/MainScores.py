from Utils import SCORES_FILE_NAME
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            content = f.read()
            return render_template("score.html", score=content)
    except FileNotFoundError as e:
        return render_template("error.html", error=e)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
