from tabulate import tabulate
from datetime import datetime
import AgeCalculate
try:
    names=str(input('enter your names: ' ))
except ValueError:
    print('this is not a name')
try:
    x=str(input('enter your fathers name: ' ))
except ValueError:
    print('this is not a name')
try:
    y=str(input('enter your mothers name: ' ))
except ValueError:
    print('this is not a name')

try:
    Ages=int(input('enter your age: '))
except ValueError:
    print('this is not an age')
try:
    q=int(input('enter your fathers age ' ))
except ValueError:
    print('this is not an age')
try:
    w=int(input('enter your mothers age ' ))
except ValueError:
    print('this is not an age')

DOB=input('enter your date of birth(must be in format dd/mm/yyyy): ' )
j=input('enter your fathers date of birth(must be in format dd/mm/yyyy): ' )
k=input('enter your mothers date of birth(must be in format dd/mm/yyyy): ' )
yourage=AgeCalculate.Age(DOB)
popsage=AgeCalculate.Age(j)
momsage=AgeCalculate.Age(k)

try:
    Places=str(input('enter your place of birth: ' ))
except ValueError:
    print('This is not a place')
try:
    a=str(input('enter your fathers place of birth ' ))
except ValueError:
    print('This is not a place')
try:
    s=str(input('enter your mothers place of birth ' ))
except ValueError:
    print('This is not a place')

data = [ ((names), (Ages), (DOB), (Places)),
         ((x), (q), (j), (a)),
         ((y), (w), (k), (s)),]

header = ['Names','Ages','DateOfBirth','Place of Birth']

if int(yourage)!=int(Ages):
    print(f'thats not your actual age it is {yourage}')

elif int(popsage)!=int(q):
    print(f'your fathers age is not correct it is {popsage}')

elif int(momsage)!=int(w):
    print(f'your mothers age is actually {momsage}')

else:
    print(tabulate(data, headers=header))


f=open("table information.txt","w+")
f.write(',Names, Ages, DOB, Places')
f.write('\n')
f.write(f'{names}, {Ages}, {DOB}, {Places}')
f.write('\n')
f.write(f'{x}, {q}, {j}, {a}')
f.write('\n')
f.write(f'{y}, {w}, {k}, {s}')
f.close()

import pandas as pd

df = pd.read_csv("table information.txt",delimiter=',')
df.to_csv('infotable.csv')