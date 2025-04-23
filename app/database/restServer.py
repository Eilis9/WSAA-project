from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from daoClass import dbDAO
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='staticpages', template_folder='../templates')

CORS(app)


#@app.route('/')
#def index():   
#    return "Electricity Unit Recording and Database! - Eilis Donohue"

@app.route('/')
def index_page():
   return render_template('index.html')

@app.route('/webviewer')
def webviewer():
    return render_template('webviewer.html')


# Plot the usage for current year (2025)
@app.route('/chart')
def chart_page(year):
    results = dbDAO.findbyyear(2025)
    labels = []
    dict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    data = []
    for result in results:
        labels.append(dict.get(result[1]))
        data.append(result[0])

    return render_template('chart.html', year=year, labels=labels, data=data)

# Updates the chart page when the dropdown is changed
@app.route('/chart_data/<int:year>')
def chart_data(year, methods=['GET']):
    results = dbDAO.findbyyear(year)  # Fetch data for the selected year
    labels = []
    month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                  7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    data = []

    for result in results:
        labels.append(month_dict.get(result[1]))
        data.append(result[0])

    return jsonify({'labels': labels, 'data': data})

# Get all entries in the unit table
@app.route('/elec/units', methods=['GET'])
def getall():
    #table = 'unit'
    results = dbDAO.getAll()
    print("flask", results)
    return jsonify(results)

# Get all entries in the cost code table
@app.route('/elec/cc', methods=['GET'])
def getallCodes():
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