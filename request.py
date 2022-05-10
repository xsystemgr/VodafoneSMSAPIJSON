from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
  {"id":"campaign-id","recipient":"msisdn","status":"status-string","error": 80}
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204