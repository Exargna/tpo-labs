from flask import Flask, jsonify, request

app = Flask(__name__)
users = [{"id": 1, "name": "Admin", "email": "admin@test.com"}]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    new_id = len(users) + 1
    user = {"id": new_id, "name": data.get("name", ""), "email": data.get("email", "")}
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
