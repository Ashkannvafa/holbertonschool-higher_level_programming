#!/usr/bin/python3
"""Display product data from JSON or CSV files in Flask."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    with open("products.json", "r") as f:
        return json.load(f)


def read_csv():
    """Read products from CSV file."""
    with open("products.csv", "r") as f:
        return list(csv.DictReader(f))


@app.route("/products")
def products():
    """Display products from selected source."""
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    products_list = []

    if source == "json":
        products_list = read_json()
    elif source == "csv":
        products_list = read_csv()
    else:
        error = "Wrong source"

    if not error and product_id:
        products_list = [
            product for product in products_list
            if str(product.get("id")) == product_id
        ]

        if not products_list:
            error = "Product not found"

    return render_template(
        "product_display.html",
        products=products_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
