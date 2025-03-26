from flask import Flask, url_for, request, redirect, abort
from daoClass import dbDAO



app = Flask(__name__, static_url_path='', static_folder= 'staticpages')

@app.route('/')
def index():
    
    return "hello there"



@app.route('/elec', methods=['GET'])
def getall():
    results = dbDAO.getAll()
    print("debug")
    return str(results)

@app.route('/elec/<int:id>', methods=['GET'])
def findbyid(id):
    results = dbDAO.findbyid(id)
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

# update
@app.route('/elec/<int:id>', methods=['PUT'])
def update(id):
    # read json from the body
    jsonstring = request.json
    return f"update {id} {jsonstring}"

# delete
@app.route('/elec/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == '__main__':
    app.run(debug=True)