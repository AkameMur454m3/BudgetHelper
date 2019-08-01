def calculateBudget(salary, housing, medical, car, stateTax):
    return salary - stateTax/100 * salary - housing*12 - medical*12 - car*12
    
def calulateHousing(housing):
    return housing*12
    
def calulateMedical(medical):
    return medical*12
    
def salary(salary):
    return salary
    
def carPay(car):
    return car*12
    
def stateTax(stateTax, salary):
    return stateTax/100 * salary