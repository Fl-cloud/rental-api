from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
properties = [
    {"id": 1, "name": "Sunset Villa", "location": "Orlando", "available": True},
    {"id": 2, "name": "Ocean View Apartment", "location": "Miami", "available": False}
]

# GET all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

# POST a new property
@app.route('/properties', methods=['POST'])
def add_property():
    new_property = request.get_json()
    new_property['id'] = len(properties) + 1
    properties.append(new_property)
    return jsonify(new_property), 201

if __name__ == '__main__':
    app.run(debug=True)