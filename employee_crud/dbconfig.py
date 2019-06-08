#from employee_crud.controller import config as app
#from employee_crud.dbcontroller import config as app
from flask_sqlalchemy import SQLAlchemy  #orm
from flask import Flask
from employee_crud.appstart import config as app

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Employee(db.Model): # orm Model
   id = db.Column('emp_id', db.Integer, primary_key = True)
   name = db.Column('emp_name', db.String(100))
   city = db.Column('emp_address', db.String(50))
   age = db.Column('emp_age', db.Integer)
   salary = db.Column('emp_sal', db.Float())
   designation = db.Column('emp_post', db.String(10))

