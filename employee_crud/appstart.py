from flask import Flask
config = Flask(__name__)


from employee_crud.dbcontroller import *
from employee_crud.controller import *

if __name__ == '__main__':
    db.create_all()
    config.run(debug=True)
