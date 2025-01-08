from flask import Flask, request, jsonify
from Report import Report

app = Flask(__name__)

report_user_store = {"052111111":Report(risk_profile="052111111",update="2025-01-01T12:00:00", risk_level=0 ),
                        "054111111":Report(risk_profile="054111111",update="2024-04-01T12:00:00", risk_level=-1, is_reported=True ),
                        "056111111":Report(risk_profile="056111111",update="2023-09-01T12:00:00", risk_level=1, is_reported=True )
                        }
report_counter=3
# Create Report
#get json file end return Report
@app.route('/reports', methods=['POST'])
def create_report():
    global report_counter
    data=request.get_json()
    if not data: 
        return jsonify('ERROR: No input data provided'), 400
    report_counter+=1
    
    new_report=Report(data=data)
    report_user_store[new_report.risk_profile]=new_report
    return jsonify(new_report.to_dict()), 201

# Read Report by ID
#get report_id and return report
@app.route('/reports/<string:risk_profile>', methods=['GET'])
def get_report(risk_profile):
    report=report_user_store.get(risk_profile)
    if not report: 
        return jsonify('ERROR: Report not found'), 404 
    return jsonify(report.to_dict()), 200

# Update Report
@app.route('/reports/<string:risk_profile>', methods=['PUT'])
def update_report(risk_profile):
    report=report_user_store.get(risk_profile)
    if not report: 
        return jsonify('ERROR: Report not found'), 404 
    data = request.get_json()
    if not data: 
        return jsonify('ERROR: No input data provided'), 400
    report.update_level(data)
    return jsonify(report.to_dict()), 200

# Delete Report
@app.route('/reports/<string:risk_profile>', methods=['DELETE'])
def delete_report(risk_profile):
    report=report_user_store.pop(risk_profile,None)
    if not report:
        return jsonify('ERROR: Report not found'), 404
    return jsonify('message: Report deleted'), 200

if __name__ == "__main__":
    app.run(debug=True)