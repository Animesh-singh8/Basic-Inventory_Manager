from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
INVENTORY_FILE = 'inventory.json'

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    inventory = load_inventory()
    return jsonify(inventory)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.json
    inventory = load_inventory()
    
    # Generate new ID
    new_id = max([item['id'] for item in inventory], default=0) + 1
    
    new_item = {
        'id': new_id,
        'name': data['name'],
        'price': float(data['price']),
        'quantity': int(data['quantity'])
    }
    
    inventory.append(new_item)
    save_inventory(inventory)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    inventory = load_inventory()
    
    for item in inventory:
        if item['id'] == item_id:
            item['name'] = data['name']
            item['price'] = float(data['price'])
            item['quantity'] = int(data['quantity'])
            save_inventory(inventory)
            return jsonify(item)
    
    return jsonify({'error': 'Item not found'}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    inventory = load_inventory()
    inventory = [item for item in inventory if item['id'] != item_id]
    save_inventory(inventory)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)
