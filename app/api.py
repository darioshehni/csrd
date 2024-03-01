from flask import Flask, request, jsonify


app = Flask(__name__)


stakeholders = []  # Simulated in-memory 'database'
id_counter = 1  # Counter to simulate auto-incrementing primary key


@app.route('/stakeholders', methods=['GET'])
def get_stakeholders():
    """Retrieve a list of all stakeholders."""
    return jsonify(stakeholders)


@app.route('/stakeholder', methods=['POST'])
def add_stakeholder():
    """Add a new stakeholder and return the added stakeholder with its new ID."""
    global id_counter
    stakeholder = request.json
    stakeholder['id'] = id_counter
    id_counter += 1
    stakeholders.append(stakeholder)
    return jsonify(stakeholder), 201


@app.route('/stakeholder/<int:stakeholder_id>', methods=['PUT'])
def update_stakeholder(stakeholder_id):
    """Update an existing stakeholder's information by ID."""
    stakeholder = next((s for s in stakeholders if s['id'] == stakeholder_id), None)
    if not stakeholder:
        return jsonify({'message': 'Stakeholder not found'}), 404
    data = request.json
    stakeholder.update(data)
    return jsonify(stakeholder)


@app.route('/stakeholder/<int:stakeholder_id>', methods=['DELETE'])
def delete_stakeholder(stakeholder_id):
    """Delete a stakeholder by ID."""
    global stakeholders
    stakeholders = [s for s in stakeholders if s['id'] != stakeholder_id]
    return jsonify({'message': 'Stakeholder deleted'})


if __name__ == '__main__':
    app.run(port=8000, debug=True)