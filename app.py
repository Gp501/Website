#import os
#from flask import Flask, jsonify, render_template
#
#app = Flask(__name__)
#
## A simple in-memory "database" for this 3-tier demo
#items_data = [
#    {"id": 1, "name": "Integrated Item A"},
#    {"id": 2, "name": "Integrated Item B"},
#    {"id": 3, "name": "Integrated Item C"}
#]
#
## Root route serves the frontend HTML page
#@app.route('/')
#def index():
#    # Flask automatically looks in the 'templates' folder for this file
#    return render_template('index.html')
#
## API endpoint returns JSON data
#@app.route('/api/items', methods=['GET'])
#def get_items():
#    return jsonify(items_data)
#
## Run the app using the PORT environment variable provided by Azure
#if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 80))
#    app.run(host='0.0.0.0', port=port)
#

#====================================================#
#import os
#from flask import Flask, jsonify, render_template
#
#app = Flask(__name__)
#
#items_data = [
#    {"id": 1, "name": "RAM"},
#    {"id": 2, "name": "Krishna"},
#    {"id": 3, "name": "Hari !!"}
#]
#
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#@app.route('/api/items', methods=['GET'])
#def get_items():
#    return jsonify(items_data)
#
# No need for app.run() here for Azure, 
# Gunicorn handles the port and host automatically.
#====================================================#

"""# Addable the Iteam 
import os
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory "database" 
items_data = [
    {"id": 1, "name": "RAM"},
    {"id": 2, "name": "Krishna"},
    {"id": 3, "name": "Hari !!"}
]

# Helper function to generate unique IDs for new items
def get_next_id():
    return max(item['id'] for item in items_data) + 1 if items_data else 1

# Root route serves the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint returns JSON data (GET)
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items_data)

# API endpoint to ADD data (POST)
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item_data = request.get_json() # Get JSON data sent from JavaScript
    if new_item_data and 'name' in new_item_data:
        new_item = {
            "id": get_next_id(),
            "name": new_item_data['name']
        }
        items_data.append(new_item) # Add to our list
        return jsonify(new_item), 201 # Return the new item and 201 Created status
    return jsonify({"error": "Invalid data provided"}), 400

# NOTE: You still need the Azure Portal settings and requirements.txt from previous steps!
"""

import os
from flask import Flask, jsonify, render_template, request, abort

app = Flask(__name__)

# A simple in-memory "database" 
items_data = [
    {"id": 1, "name": "RAM"},
    {"id": 2, "name": "Krishna"},
    {"id": 3, "name": "Hari !!"}
]

def get_next_id():
    return max(item['id'] for item in items_data) + 1 if items_data else 1

@app.route('/')
def index():
    return render_template('index.html')

# API endpoint returns JSON data (GET)
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items_data)

# API endpoint to ADD data (POST)
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item_data = request.get_json()
    if new_item_data and 'name' in new_item_data:
        new_item = {
            "id": get_next_id(),
            "name": new_item_data['name']
        }
        items_data.append(new_item)
        return jsonify(new_item), 201
    return jsonify({"error": "Invalid data provided"}), 400

# API endpoint to DELETE data (DELETE)
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item_to_delete = next((item for item in items_data if item['id'] == item_id), None)
    
    if item_to_delete:
        items_data.remove(item_to_delete)
        return jsonify({"message": f"Item {item_id} deleted"}), 200
    else:
        # Return 404 Not Found if the ID doesn't exist
        abort(404, description="Item not found")

# NOTE: Remember your requirements.txt and Azure Portal settings!
