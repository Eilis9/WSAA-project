# Web Services and Applications Project

The project undertaken for the Web Services and Applications module as part of the HDip in Computing in Data Analytics (ATU).


Student Name: Eilis Donohue <br>
Student Number: G00006088 <br>
Lecturer: Andrew Beatty <br>

### Project Description
The project is a web application that allows users to create/update/delete electricity readings and cost codes related to the price of electricity. Data is stored in a MySQL database. The application is built using Flask, and utilises Bootstrap for styling and Chart.js for data visualisation.  

### Hosting

The application is hosted on PythonAnywhere. See [https://eilis9.pythonanywhere.com/](https://eilis9.pythonanywhere.com/)


### MySQL Database
A MySQL database of electricity readings and cost codes is used to store the data (/app/database/elec.sql). The database connection details should be created in a file called app/database/dbconfig.py.

The database comprises two tables:
1. Unit
2. Cost

The cost code is a foreign key in the unit table. 
Cost codes must be unique in the cost table. 

The database schema is represented here:

<img src="app\img\database_schema.PNG" alt="Database Schema" width="600"/>


### Webviewer
The webviewer is a web application built using HTML, ajax and jquery, Flask, Bootstrap, and Chart.js. It allows users to view the reading and cost code data in table format.  The main table at /webviewer is a combination of the data from both of the MySQL tables.  Each unit reading and cost code entry may be updated or deleted. A new reading or cost code may be entered. 

The navigation bar at the top of the webviewer allows users to navigate to different pages. A chart and calculation is also included as part of the webviewer.

### CRUD Functionality

A new electricity reading or cost code may be created by clicking on the "Create" button in the top right corner of the webviewer.  

Data validation occurs in the DAO class and the Flask app. 

A new electricity reading must have a unique year and month entry (i.e., duplicate entries are not permitted). The user is prompted to enter a new year and month if the entry already exists. Invalid  month entries are also rejected with an error message.  

The cost code entered for a new electricity reading must have an existing cost code in the cost table in the database.

A new cost code may be created by clicking on the "Create" button in the top right corner of the webviewer.  The cost code must be unique.

Each entry in the tables displayed by the webviewer may be updated or deleted.

### API Endpoints

The CRUD endpoints are available:

| Endpoint         | Method | Description / Request Body         |
|------------------|--------|------------------------------------|
| `/elec/units`          | GET    | Get all electricity readings with associated cost code details |
| `/elec`          | POST   | Create a new reading (JSON object containing 'year', 'month', 'units', 'cost_code') |
| `/elec/<int:id>`     | PUT    | Update a reading (JSON object containing 'id', 'year', 'month', 'units', 'cost_code') |
| `/elec/<int:id>`     | DELETE | Delete a reading                   |
| `/elec/cost_codes` | GET  | Get all cost codes                 |
| `/elec/cost_codes` | POST | Create a new cost code (JSON object containing 'cost_code', 's_charge', 'unit_cost', 'vat_pc', 'supplier')      |      |
| `/elec/cost_codes/<string:cost_code>` | PUT | Update a cost code based on id (JSON object containing 'id', 'cost_code', 's_charge', 'unit_cost', 'vat_pc', 'supplier')      |
| `/elec/cost_codes/<string:cost_code>` | DELETE | Delete a cost code based on ID      |


### Analysis and Visualisation

***Visualisation***
The electricity readings may be visualised by navigating to /chart (accessed under Analysis on the navbar). The chart displays each year by selecting from the dropdown. In addition, the mean temperature at the Athenry weather station is displayed. This data is obtained from the Met Eireann API (https://prodapi.metweb.ie/monthly-data/Athenry). Temperature data only exists from 2022 onwards. 


***Cost Calculation***
The cost of electricity for a given time period may be calculated by navigating to /webviewer/analysis. The user fills in the start and end dates and the total cost is calculated using the elec and cost tables. Cost in euros is displayed.


### How to run the app
The app may be viewed and used at [https://eilis9.pythonanywhere.com/](https://eilis9.pythonanywhere.com/)

It may be run locally by:

1. Set up a MySQL database and load the MySQL file app\database\elec.sql.  The database connection details should be created in a file called app\database\dbconfig.py.

2. Cloning the repository to your local machine: 
```bash
git clone https://github.com/Eilis9/WSAA-project.git
```
2. Creating a virtual environment:
```bash
python -m venv venv
```
3. Activating the virtual environment:
```bash
source venv/bin/activate
```
4. Installing the required packages:
```bash
pip install -r requirements.txt
```
5. The app may then be launched by running the file:
```bash
python app/database/restServer.py
```
6. Open a web browser and navigate to http://127.0.0.1:5000/


### References / Resources

- Andrew Beatty Github. [Online] Available: https://github.com/andrewbeattycourseware/deploytopythonanywhere 

- W3 Schools. Bootstrap 5 Tutorial [Online] Available: https://www.w3schools.com/bootstrap5/

- Get Boostrap. Navbar [Online] Available: https://getbootstrap.com/docs/5.3/components/navbar/

- Bootstrap Table. Filters [Online] Available: https://bootstrap-table.com/docs/extensions/filter-control/

- Github cpryan. Tables [Online] Available: https://cpryan.github.io/blog/2023/tables/

- W3 Schools. Navbar [Online] Available: https://www.w3schools.com/bootstrap5/bootstrap_navbar.php

- Geeks for Geeks. Chart.js [Online] Available: https://www.geeksforgeeks.org/how-to-add-graphs-to-flask-apps/

- Chart js. Multiple axes [Online] Available: https://www.chartjs.org/docs/latest/samples/line/multi-axis.html

- Stack Overflow. Setting chart title and axes [Online] Available: https://stackoverflow.com/questions/27910719/in-chart-js-set-chart-title-name-of-x-axis-and-y-axis