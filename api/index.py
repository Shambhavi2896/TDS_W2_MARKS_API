from flask import Flask, request, jsonify
import json
import os

app = Flask(_name_)

# Load student data from the JSON file
def load_data():
    # Ensure the correct path to the JSON file
    with open(os.path.join(os.getcwd(), 'students.json'), 'r') as file:
        data = json.load(file)
    return data

@app.route('/api', methods=['GET'])
def get_marks():
    # Get 'name' parameters from the query string
    names = request.args.getlist('name')

    # Load data from the JSON file
    data = load_data()

    # Prepare the result dictionary
    result = {"marks": []}
    for name in names:
        # Find the marks for each name
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])

    # Return the JSON response with CORS headers enabled
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')  # Enable CORS for any origin
    return response

if _name_ == '_main_':
    app.run()