from flask import request,render_template
from employee_crud.emp_info import Employee
from employee_crud.appstart import config

listOfEmps = []

@config.route("/index/",methods=["GET"])
def welcome():
    #return "welcome to flask web application"
    return render_template('empinfo.html',employees = listOfEmps,oneemp=dummyemp())


@config.route("/edit/<int:eid>")
def edit_emp(eid):
    oneemp = None
    for emp in listOfEmps:
        if emp.empId == eid:
            oneemp=emp
    return render_template('empinfo.html', employees=listOfEmps,oneemp=oneemp)

def dummyemp():
    return Employee(eid=0,enm='',eag=0,esal=0.0,eadr='',edeg='')

@config.route("/delete/<int:eid>")
def delete_emp(eid):
    for emp in listOfEmps:
        if emp.empId==eid:
            listOfEmps.remove(emp)
    return render_template('empinfo.html', employees=listOfEmps,oneemp=dummyemp())


counter = 1
@config.route("/saveemp/",methods=["POST"])
def emp_persist():
    global counter
    #print(request.form)
    #print(request.args)
    #return 'emp persist method invoked...!'
    if int(request.form['empid'])>0:
       for emp in listOfEmps:
           if emp.empId==int(request.form['empid']):
               emp.empName=request.form['empnm']
               emp.empAge = request.form['empag']
               emp.empAddress = request.form['empadr']
               emp.empSalary = request.form['empsal']
               emp.empDegignation = request.form['empdesg']
    else:
        emp = Employee(eid=counter,
                 enm=request.form["empnm"],
                 eag=request.form["empag"],
                 esal=request.form["empsal"],
                 eadr=request.form["empadr"],
                 edeg=request.form["empdesg"])
        listOfEmps.append(emp)
    counter+=1
    print(listOfEmps)
    return render_template('empinfo.html',employees = listOfEmps,oneemp=dummyemp())

@config.route("/abc")
def abcd():
    return "hello ...welcome to python..!...good morning..!"
