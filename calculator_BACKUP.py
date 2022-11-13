# -*- coding: utf-8 -*-`s
"""
Created on Fri Aug 21 10:57:55 2020
This program demonstrates the use of Zach's calculator
@author: zach
"""

import math
from colorama import Fore, Back, Style

calculateAbles = [
"C: area of a circle,"
"R: area of a rectangle,"
"S: area of a square,"
]

pi = 3.14
area =  -0
answer = -0

print('Welcome to Zachs calculator program zach has requested for me to calculate your area of a square rectangle or circle  and to do your perimiter and conversions did i spell that right anyway proceed')
zcode = input ("choose: s, r,c,yf, fi,mm,pr,ps,pc\n")
if zcode =="pr":
 try:
    radius =float(input ('enter radius'))  
    perimiter = 3.14159
    print(perimiter)
 except:
  print('this is not valid for zachs calculatorbot')

elif zcode =="ps":
 try:
       length = float (input ('enter length'))  
       perimiter = length*length
 except:     
       print('what is this falsness')
elif zcode =="pr":
 try:
       length = float (input ('enter length'))  
       width = float (input ('enter length'))
       perimiter = length*width
 except:
  print('this is not valid for zachs calculatorbot')
elif zcode == "mm":
    try:
        meters =float( input("enter amount of miles:  \n"))
        answer = meters*0.91443
        print("your answer is",answer)
    except:
        print('this is not valid for zachs calculator')
elif zcode == "mm":
    try:
        meters =float( input("enter amount of miles:  \n"))
        answer = meters*1609.34
        print("your answer is",answer)
    except:
        print('this is not valid for zachs calculator')
elif zcode == "c":
    try:
        radius = float( input("enter  radius:  \n"))
        area=pi*radius*radius
        areaTest = pi * math.pow(radius,2)
    except:
        print('this is not valid for zachs calculator')
elif zcode == "yf":
    try:
        yards =float( input("enter amount of yards:  \n"))
        answer = yards*12
        print("your answer is",answer)
    except:
        print('this is not valid for zachs calculator')
elif zcode == "fi":
    try: 
        feet =float( input("enter amount of feet:  \n"))
        answer = feet*12
        print("your answer is",answer)
    except:
        print('this is not valid for zachs calculator')
elif zcode == "s":
    try:   
      side=float(input('enter side:\n'))
      area=side*side
    except:
        print('this is not valid for zachs calculator')   
elif zcode == "r":
    try:
      length = float(input('enter length:\n'))
      width = float(input('enter width:\n'))
      if length == width:
          print(Fore.CYAN,'this is a square just a f.y.i.')
          area = length*width
          print(area)
      else:
          print('this is a rectangle')
          area = length*width
          print(area)
    except:
          print('this is not valid for zachs calculator')      
else:
  print('this is not valid for zachs calculator')
print('your area is', area) 
print(Style.RESET_ALL)