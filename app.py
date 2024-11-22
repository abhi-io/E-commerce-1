from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample product data (in a real application, you might fetch this from a database)
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699.99},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 19.99},
    {"id": 4, "name": "Jeans", "category": "Clothing", "price": 49.99},
    {"id": 5, "name": "Headphones", "category": "Electronics", "price": 129.99},
    {"id": 6, "name": "Coffee Maker", "category": "Home Appliances", "price": 89.99},
    {"id": 7, "name": "Vacuum Cleaner", "category": "Home Appliances", "price": 150.00},
    {"id": 8, "name": "Sofa", "category": "Furniture", "price": 799.99}
]

@app.route('/')
def index():
    return "Welcome to the Product API!"

@app.route('/products', methods=['GET'])
def get_products():
    # Get filter parameters from the request
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    search = request.args.get('search')

    filtered_products = products

    # Filter by category
    if category:
        filtered_products = [p for p in filtered_products if p['category'].lower() == category.lower()]

    # Filter by price range
    if min_price is not None:
        filtered_products = [p for p in filtered_products if p['price'] >= min_price]
    
    if max_price is not None:
        filtered_products = [p for p in filtered_products if p['price'] <= max_price]
    
    # Filter by search term (name contains the search term)
    if search:
        filtered_products = [p for p in filtered_products if search.lower() in p['name'].lower()]

    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True)

