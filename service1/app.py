from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'unauthorized'}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

