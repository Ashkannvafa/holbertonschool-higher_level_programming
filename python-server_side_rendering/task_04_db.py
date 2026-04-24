#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite in Flask."""
import csv
import json
import sqlite3
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


def read_sql():
    """Read products from SQLite database."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        }
        for row in rows
    ]


@app.route("/products")
def products():
    """Display products from selected source."""
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    products_list = []

    try:
        if source == "json":
            products_list = read_json()
        elif source == "csv":
            products_list = read_csv()
        elif source == "sql":
            products_list = read_sql()
        else:
            error = "Wrong source"
    except sqlite3.Error:
        error = "Database error"

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
