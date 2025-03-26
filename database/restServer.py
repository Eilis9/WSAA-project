from flask import Flask, url_for, request, redirect, abort
from daoClass import dbDAO


app = Flask(__name__, static_url_path='', static_folder= 'staticpages')

@app.route('/')
def index():
    
    return "Electricity Unit Recording and Database! - Eilis Donohue"


@app.route('/elec', methods=['GET'])
def getall():
    results = dbDAO.getAll()
    print("debug")
    return str(results)

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
    #print(request.json)
    values = list(jsonstring.values()) 
    dbDAO.create(values)

    return f"create {jsonstring}"

# update an entry based on year and month
@app.route('/elec', methods=['PUT'])
def update_unit():
    # read json from the body
    jsonstring = request.json
    # Extract values from the jsonstring to put in correct order
    year = jsonstring.get('year')
    month = jsonstring.get('month')
    unit = jsonstring.get('unit')
    cost_code = jsonstring.get('cost_code')
    values= [unit, cost_code, year, month]
    dbDAO.update_unit(values) 
    return f"update {jsonstring}"

# delete based on year and month
@app.route('/elec', methods=['DELETE'])
def delete():
    year = request.args.get('year', type=int)  # Get 'year' from query parameters
    month = request.args.get('month', type=int)  # Get 'month' from query parameters
    return f"delete entry for {year} {month}"

if __name__ == '__main__':
    app.run(debug=True)