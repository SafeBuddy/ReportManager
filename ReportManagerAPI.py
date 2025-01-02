from flask import Flask, request, jsonify
from Report import Report

app = Flask(__name__)

reports_store = {}
report_id_counter=0

# Create Report
#get json file end return Report
@app.route('/reports', methods=['POST'])
def create_report():
    global report_id_counter
    data=request.get_json()
    if not data: 
        return jsonify('ERROR: No input data provided'), 400
    report_id_counter+=1
    
    report=Report(report_id_counter, data)
    reports_store[report_id_counter]=report
    return jsonify(report.to_dict()), 201

# Read Report by ID
#get report_id and return report
@app.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    report=reports_store.get(report_id)
    if not report: 
        return jsonify('ERROR: Report not found'), 404 
    return jsonify(report.to_dict()), 200

# Update Report
@app.route('/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    report=reports_store.get(report_id)
    if not report: 
        return jsonify('ERROR: Report not found'), 404 
    data = request.get_json()
    if not data: 
        return jsonify('ERROR: No input data provided'), 400
    report.update(data)
    return jsonify(report.to_dict()), 200

# Delete Report
@app.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    report=reports_store.pop(report_id, None)
    if not report:
        return jsonify('ERROR: Report not found'), 404
    return jsonify('message: Report deleted'), 200

