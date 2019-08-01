from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
     return render_template("index.html")
@app.route('/results',methods=['GET','POST'])
def results():
    moneyLeft=model.calculateBudget(int(request.form['salary']), int(request.form['housing']), int(request.form['medical']), int(request.form['car']), int(request.form['stateTax']))
    housing=model.calulateHousing(int(request.form['housing']))
    medical=model.calulateMedical(int(request.form['medical']))
    salary=model.salary(int(request.form['salary']))
    car=model.carPay(int(request.form['car']))
    stateTax=model.stateTax(int(request.form['stateTax']), int(request.form['salary']))
    return render_template("results.html",moneyLeft=moneyLeft, housing=housing, medical=medical, salary=salary, car=car, stateTax=stateTax)