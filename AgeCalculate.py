from datetime import datetime

def Age(dob):
    thedate=datetime.strptime(dob, '%d/%m/%Y')
    theage =2020-thedate.year
    return theage

