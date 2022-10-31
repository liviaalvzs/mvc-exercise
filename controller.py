from flask import Flask
from models.product import Product

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'Hello World!'

@app.route('/v1/product/', methods=["GET"])
def index():
    return Product.json_return()


@app.route('/v1/product/total', methods=["GET"])
def total():
    return Product.total()

@app.route('/v1/product/discount', methods=["GET"])
def discount_prices():
    return Product.discount_prices()


if __name__ == '__main__':
    app.run(debug=True,port= 5000)