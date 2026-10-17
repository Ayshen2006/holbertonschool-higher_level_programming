#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, name, category, price FROM Products'
        )
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
    except (OSError, json.JSONDecodeError, sqlite3.Error, csv.Error):
        return render_template(
            'product_display.html',
            products=[],
            error='Error reading data source'
        )

    if product_id is not None:
        data = [
            product for product in data
            if str(product.get('id')) == product_id
        ]

        if not data:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
