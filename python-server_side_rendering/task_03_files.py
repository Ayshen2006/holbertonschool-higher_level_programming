#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    data = read_json() if source == 'json' else read_csv()

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
