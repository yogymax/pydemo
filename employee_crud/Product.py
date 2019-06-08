from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pydb'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(application)


class Product_Info(db.Model): # orm Model
   id = db.Column('product_id', db.Integer, primary_key = True)
   name = db.Column('product_name', db.String(100))
   cat = db.Column('product_category', db.String(50))
   qty = db.Column('product_qty', db.Integer)
   price = db.Column('product_price', db.Float())
   desc = db.Column('product_remarks', db.String(50))

   def __str__(self):
       return f'\n {self.__dict__}'

   def __repr__(self):
       return str(self)


