#NUMPY is used for numerical computation with python, PANDAS is used for analysing tabular data, it is like working with spreadsheets but we are writing codes here, MATPLOITLIB and SEABORN are used for data visualization, graphs, line graph, bar chart etc


calculated=5 + True      
#print(calculated)


#ASK CHAT GPT FOR NESTED LOOPS IN PYTHON
#for us to filter thhe even numbers in the list provided below
def filterEven(values):
    resultingvalues=[]
    for i in values:
        if i%2==0:
            resultingvalues.append(i)
    return resultingvalues
print(filterEven([2,3,4,5,6,7,8,9,10,11,12,13,14]))



#codes for certain functions in mathematics
#A python code to convert degrees to Radians
from math import pi
def degtorad(degg):
    return ((pi * degg )/(180))
print(degtorad(15))


#A python code to convert Radian to Degree
def radtodeg(radd):
    return ((180 * radd )/(pi))
print(radtodeg(.52))



#Python code to calculate the area of a trapezoid
def areaoftrap(base1,base2,height):
    return(0.5*(base1+base2)*height)
print(areaoftrap(5,6,5))


#Python code to calculate the area of a parallelogram
def areaofparrallelogram(b,h):
    return (b * h)
print(areaofparrallelogram(5,6))


#Python code to calculate the surface area of and volme of a sphere
#Volume of a sphere
def volofsphere(radius):
    return ((4/3)* pi * (radius)**3)
print(volofsphere(0.75))
#Area of a sphere
def areaofsphere(radius2):
    return (4*pi*(radius2)**2)
print(areaofsphere(.75))


#Python code to calculate the area of sector
def areaofsector(thetha, Diameter):
    return ((thetha/360)* pi *(Diameter/2)**2)
print((areaofsector(45,8)))




#python code to calculate the discriminant value of numbers
def discriminatvalue(a,b,c):
    return ((b**2)-(4*a*c))
print(discriminatvalue(4,0,-1))




#python code for the sum of all the divisor of a number is given as





#a function to add all the divisors of a positive number
def adddivisor(thenumber):
    if thenumber<0:
        return "enter a positive number!"
    emptylist=[]
    for i in range(1,thenumber+1):
        if thenumber%i==0:
            emptylist.append(i)
    return sum(emptylist)   #note where the return is, that it is directly below the name of the function that we defined
print(adddivisor(-23))




#Python code to compute the square root of any number
import math
def sqrnumber(mynum):
    if mynum<0:
        return ('please enter a number greater than 0')
    else:
        return (math.sqrt(mynum))
print(sqrnumber(32))


#Python code to multiply two integers;
def multiinteger(a,b):
    return (a*b)
print(multiinteger(3,15))




#Python program to find the root of a quadratic function
import cmath   #means complex math module
def quadraticfunc(a,b,c):
    dis=b**2 - 4*a*c
    root1=(-b+cmath.sqrt(dis))/(2*a)
    root2=(b-cmath.sqrt(dis))/(2*a)
    return (root1, root2)

print(quadraticfunc(2,3,4))



#a python function to convert a decimal number to a binary number using the inbuilt bin function:
def dectobin(n):
    step1=bin(n)
    step2=step1[2:]
    return step2
print(dectobin(34))



#a python function to add two complex number together, same method goes for other operations like subtract, divide etc
a=complex(3,4)
b=complex(10,5)
print(a+b)





#a python code that returns the imaginary and the real parts of a complex number
compy=complex(3,4)
rely=compy.real   #notice this
com=compy.imag     #notice this
rsult=(rely, com,'j')





#a python code to get the length of a complex number
compy2=complex(-2,4)
firstside=compy2.real
secondside=compy2.imag
finalResult=((firstside**2) + (secondside**2))
print(finalResult)



import math
#a python code to get the angle in a comple number
compy3=complex(-2,4)
firstside=abs(compy2.real)
secondside=abs(compy2.imag)
value=firstside/secondside
result=math.degrees(math.atan(value))
print(result)



#a python code to find the maximum and the minimum of a list of numbers
mynum=12,23,45,67, 4000.890,899,922
print(max(mynum))
print(min(mynum))



#a python code to find the sum of a list of numbers
lst=[23,30.33,10,22.456,200.22,78.99]
print(sum(lst))


#a python program to get the square root and the exponential of a given number
numberr=23.1
print(math.exp(numberr))


















        


        








