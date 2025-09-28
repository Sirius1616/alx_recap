#!/usr/bin/env python
from flask import Flask, jsonify, make_response


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
        print("Item with {} already exists".format(item_id))
        return
    else:
        if not item_id[0]:
            return make_response(jsonify({'error': 'Item not added'}))
        added = items.append(item_id)
        return jsonify({'added': added})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


