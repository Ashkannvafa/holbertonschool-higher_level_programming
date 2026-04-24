#!/usr/bin/python3
"""Flask app that renders items from a JSON file."""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render home page."""
    return render_template("index.html")


@app.route("/items")
def items():
    """Render items page using data from items.json."""
    with open("items.json", "r") as f:
        data = json.load(f)

    return render_template("items.html", items=data.get("items", []))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
