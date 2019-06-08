from employee_crud.emp_info import Employee
from employee_crud.dbconfig import Employee as EmpModel,db
from flask import request,render_template
from employee_crud.appstart import config

print('inside db controller...!')
def dummyemp():
    return EmpModel(id=0,name='',age=0,salary=0.0,city='',designation='')




@config.route("/welcome/", methods=["GET"])
def welcome_db_save():
    return render_template('dbempinfo.html', oneemp=dummyemp(),employees= EmpModel.query.all())



@config.route("/persist/", methods=["POST"])
def save_into_db():
    print(request.form)
    if int(request.form['empid'])>0:
        dbEmp = EmpModel.query.filter_by(id=request.form['empid']).first()
        dbEmp.name=request.form['empnm']
        dbEmp.age = request.form['empag']
        dbEmp.salary = request.form['empsal']
        dbEmp.city = request.form['empadr']
        dbEmp.designation = request.form['empdesg']
        db.session.commit()
    else:
        emodel = EmpModel(name=request.form["empnm"],
             city=request.form["empadr"],
             age=request.form["empag"],
             salary=request.form["empsal"],
             designation=request.form["empdesg"])
        db.session.add(emodel)
        db.session.commit()

    return render_template('dbempinfo.html', oneemp=dummyemp(),employees= EmpModel.query.all())


@config.route("/oneemp/<int:eid>",methods=["GET"])
def fetch_emp(eid):
    singleEmp = EmpModel.query.filter_by(id=eid).first()
    allEmps = EmpModel.query.all()
    return render_template('dbempinfo.html', employees=None, oneemp=dummyemp())

@config.route("/allemps/",methods=["GET"])
def fetch_all_emps():
    return render_template('dbempinfo.html', employees=None, oneemp=dummyemp())


@config.route("/modify/<int:eid>",methods=["GET"])
def modify_emp(eid):
    singleEmp = EmpModel.query.filter_by(id=eid).first()
    print(singleEmp)
    return render_template('dbempinfo.html', employees=EmpModel.query.all(), oneemp=singleEmp)


@config.route("/remove/<int:eid>",methods=["GET"])
def remove_emp(eid):
    singleEmp = EmpModel.query.filter_by(id=eid).first()
    db.session.delete(singleEmp)
    allEmps = EmpModel.query.all()
    return render_template('dbempinfo.html', employees=allEmps, oneemp=dummyemp())



