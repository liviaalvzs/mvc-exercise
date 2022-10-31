import json

products = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "Powerful laptop for programmers!",
        "price": 4999.99,
        "discount": 10
    },
    {
        "id": 2,
        "name": "Notebook",
        "description": "To write a lot of things :)",
        "price": 15,
        "discount": 5
    },
    {
        "id": 3,
        "name": "Iphone",
        "description": "Take beautiful pictures!",
        "price": 4000,
        "discount": 15
    }
]

productsJSON = json.dumps(products)

class Product():

    def json_return():
        return productsJSON
    
    def total():
        sum = 0
        for p in products:
            sum += p.get("price")
        return {
            "total_price": sum
        }
    
    def discount_prices():
        sum = 0
        prices = []
        for p in products:
            discount = p.get("discount")
            price = p.get("price")
            total = price - (price * (discount/100))
            prices.append(total)
        return {
            "product_1": prices[0],
            "product_2": prices[1],
            "product_3": prices[2],
        }