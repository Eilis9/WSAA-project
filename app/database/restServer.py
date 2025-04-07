from flask import Flask, url_for, request, redirect, abort, jsonify
from daoClass import dbDAO
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder= 'staticpages')
CORS(app)
@app.route('/')
def index():   
    return "Electricity Unit Recording and Database! - Eilis Donohue"
@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/elec', methods=['GET'])
def getall():
    #table = 'unit'
    results = dbDAO.getAll()
    print("flask", results)
    return jsonify(results)

# find an entry based on year and month query parameters
@app.route('/elec/find', methods=['GET'])
def findbyid():
    year = request.args.get('year', type=int)  
    month = request.args.get('month', type=int)  
    print(f"Debug: year={year}, type={type(year)}")
    print(f"Debug: month={month}, type={type(month)}")
    results = dbDAO.findbyid(year, month)
    return results

#create
@app.route('/elec', methods=['POST'])
def create():
    # read json from the body
    jsonstring = request.json
    reading = {}
    #TODO : put in conditions here based on blanks
    reading["year"] = jsonstring["year"]
    reading["month"] = jsonstring["month"]
    reading["unit"] = jsonstring["unit"]
    reading["cost_code"] = jsonstring["cost_code"]

    print("server", request.json)


    return jsonify(dbDAO.create(reading))

# update an entry based on id
@app.route('/elec/<int:id>', methods=['PUT'])
def update_unit(id):
    # read json from the body
    print("jsonstring in flask", request.json)
    jsonstring = request.json
    reading = {}
    print("reading in server", jsonstring)
    # Extract values from the jsonstring to put in correct order
    reading['id'] = id
    reading["year"] = jsonstring["year"]
    reading["month"] = jsonstring["month"]
    reading["unit"] = jsonstring["unit"]
    reading["cost_code"] = jsonstring["cost_code"]
    print("flask", reading)
    return jsonify(dbDAO.update_unit(id, reading)) 

# delete based on id
@app.route('/elec/<int:id>', methods=['DELETE'])
def delete(id):
    
    return jsonify(dbDAO.delete(id))

if __name__ == '__main__':
    app.run(debug=True)