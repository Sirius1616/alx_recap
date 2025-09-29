#!/usr/bin/env python
from flask import Flask, jsonify, make_response, request


app = Flask(__name__)


items = {
    1: {'name': 'Book'},
    2: {'name': 'Laptop'},
    3: {'name': 'Phone'}
}


@app.route('/items/<int:item_id>', methods=["DELETE"])
def delete_iten(item_id):
    if item_id in items:
        deleted = items.pop(item_id)
        return jsonify({'deleted': deleted}), 200
    else:
        return make_response(jsonify({"error": "Item not found"}), 404)

@app.route('/items/<int:item_id>', methods=['POST'])
def add_item(item_id):
    if item_id in items:
        return make_response(jsonify({'Error ': f'Item with {item_id} already exist'}), 400)

    data = request.get_json()
    if not data or 'name' not in data:
            return make_response(jsonify({'error': 'Item not added'}), 400)

    items[item_id] = {'name': data['name']}
    return jsonify({'added': items[item_id]}), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def retrieve_item(item_id):
    if item_id not in items:
        return make_response(jsonify({'Error': "Item not found"}), 404)


    return jsonify({"Retrieving ...": f'item with {item_id} is given as {items[item_id]}'})

@app.route('/items/<int:item_id>', methods=['POST'])
def modify_item(item_id, ):
    if not item_id or 'name' not in item_id:
        return jsonify({"Error": f"item with {item_id} not found"}, 404)

    data = request.get_json()

    items[item_id]['email'] = data['email']

    return jsonify({"Added...": items[item_id]}, 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


