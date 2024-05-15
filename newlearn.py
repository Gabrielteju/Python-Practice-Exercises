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
    return float((b**2)-(4*a*c))
print(discriminatvalue(4,0,-4))

#python code to find the smallest multiple of the first n numbers










