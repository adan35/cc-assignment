from flask import Flask, request
from flask_restful import Resource, Api
from make_processes import make_processes
from PNGM.monitor import k_records
from PNGM.get import get_prime_nums

app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    return {"status": "success"}

class PNG(Resource):
  def post(self):
    range_json = request.get_json()
    start = int(range_json['start'])
    end = int(range_json['end'])
    make_processes(start, end)
    return {'status': 'success'}

class PNM(Resource):
  def post(self):
    k_value_json = request.get_json()
    k_value = int(k_value_json["k"])
    list = k_records(k_value)
    return {"status": "success",
            "consumptions": list}

class GAP(Resource):
  def get(self):
    lst = get_prime_nums()
    return {"status": "success",
            "prime_nums": lst}

api.add_resource(Home, '/')
api.add_resource(PNG, '/api/gen')
api.add_resource(PNM, '/api/mon')
api.add_resource(GAP, '/api/get')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")