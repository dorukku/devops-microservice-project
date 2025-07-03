from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    return jsonify([
        {"id": 1, "name": "Ürün A"},
        {"id": 2, "name": "Ürün B"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

