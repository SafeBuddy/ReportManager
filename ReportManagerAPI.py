import jsonify
from flask import *


class Flask:
    pass


app = Flask(__name__)

reports = {}

# Create Report
@app.route('/reports', methods=['POST'])
def create_report():
    return jsonify("report"), 201

# Read Report by ID
@app.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    return jsonify("Report!"), 200

# Update Report
@app.route('/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    return jsonify("Report updated"), 200

# Delete Report
@app.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    return 'Report deleted'

