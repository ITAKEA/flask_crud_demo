from flask import Flask, jsonify, request, make_response
import db
from giithub_service import merge_data


app = Flask(__name__)

# Opret database og tabel , tilføj students til db hvis tabellen er tom
db.init()

# read all
@app.route('/students')
def read_all():
    

    return jsonify(merge_data()), 200

# read one
@app.route('/students/<id>')
def read(id):
    res = db.read(id)
    if not res:
        return jsonify(message="Resource not found"), 404

    return jsonify(db.read(id)), 200


# create
@app.route('/students', methods=['POST'])
def create():
    data = request.get_json()
    id = db.create(data)
    response = make_response(jsonify(success=True, message="Resource created"), 201)
    response.headers['Location'] = f'/students/{id}'
    return response


# update
@app.route('/students/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    db.update(id, data)

    return jsonify(), 204

# patch
@app.route('/students/<id>', methods=['PATCH'])
def patch(id):
    data = request.get_json()
    return jsonify(), 204

# delete
@app.route('/students/<id>', methods=['DELETE'])
def delete(id):
    db.delete(int(id))
    return jsonify(), 204


app.run(host="0.0.0.0")