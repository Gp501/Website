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


import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

items_data = [
    {"id": 1, "Name": "RAM"},
    {"id": 2, "Name": "Krishna"},
    {"id": 3, "Name": "Hari !!"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items_data)

# No need for app.run() here for Azure, 
# Gunicorn handles the port and host automatically.
