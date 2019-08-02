from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
     return render_template("index.html")
@app.route('/results',methods=['GET','POST'])
def results():
    moneyLeft=model.calculateBudget(int(request.form['salary']), int(request.form['housing']), int(request.form['medical']), int(request.form['carPay']), int(request.form['stateTax']))
    housing=model.calulateHousing(int(request.form['housing']))
    medical=model.calulateMedical(int(request.form['medical']))
    salary=model.salary(int(request.form['salary']))
    car=model.carPay(int(request.form['carPay']))
    stateTax=model.stateTax(int(request.form['stateTax']), int(request.form['salary']))
    return render_template("results.html",moneyLeft=moneyLeft, housing=housing, medical=medical, salary=salary, car=car, stateTax=stateTax)

@app.route('/student',methods=['GET','POST'])
def student():
    salaryS=model.SalaryS(int(request.form['salaryS']))
    housingS=model.calculateHousingS(int(request.form['housingS']))
    emergencyS=model.EmergencyS(int(request.form['emergencyS']))
    transportS=model.TransportS(int(request.form['transportS']))
    bookS=model.BookS(int(request.form['bookS']))
    moneyLeftS=model.calculateBudgetStudent(int(request.form['salaryS']),int(request.form['housingS']),int(request.form['emergencyS']),int(request.form['bookS']),int(request.form['transportS']))
    return render_template("student.html",moneyLeftS=moneyLeftS, housingS=housingS, emergencyS=emergencyS, salaryS=salaryS, transportS=transportS, bookS=bookS)
