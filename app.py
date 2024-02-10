from flask import Flask, request
from functions import img_creator

app = Flask(__name__)


@app.route("/")
def index():
    prompt = request.args.get("prompt")
    size = request.args.get("size")

    if not prompt or not size:
        return "Please provide a prompt and size."

    return img_creator(prompt, size)


if __name__ == "__main__":
    app.run()