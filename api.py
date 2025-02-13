from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных о товарах
PRODUCTS = [
    {"id": 1, "name": "Говядина", "price": 500, "image": "/static/images/beef.jpg"},
    {"id": 2, "name": "Свинина", "price": 400, "image": "/static/images/pork.jpg"}
]

# Маршрут для получения товаров
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS)

# Маршрут для добавления товара
@app.route('/api/add_product', methods=['POST'])
def add_product():
    data = request.json
    PRODUCTS.append({
        "id": len(PRODUCTS) + 1,
        "name": data['name'],
        "price": data['price'],
        "image": data['image']
    })
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)