# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan
# Section: 575
# Assignment: lab 3.19 Challenge Program
# Date: 09/09/2020
#


from math import *
#>>> '{:.{}f}'.format(math.sqrt(1 - .1 **2), userDecimals)
decimalPlace = int(input("Please enter the number of digits of precision for e:\n "))
x = e
y= "{:.{}f}".format(x,decimalPlace)


print(f"The value of e to {decimalPlace} digits is: {y}")