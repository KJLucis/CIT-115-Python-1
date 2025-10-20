#Author: Katlyn Lucis    9_11_2025
#CIT-115-D02 Python Programming
#Compound Interest Calculator

#Obtain user input for variables.
#fStarting_Principal = initial amount of money in the account for which interest will be accrued upon
#fAnnual_Interest = interest rate given as a % amount, then divided by 100 to give the required decimal amount
#iCompounding = How many times per period interest is compounded
#fPeriods = how many periods, typically in years, will the pricipal accrue interest

fStarting_Principal = float(input("Enter the starting principal: "))
fAnnual_Interest = float(input("Enter the annual interest rate: "))/100
iCompounding = int(input("How many times per year is the interest compounded? "))
fPeriods = float(input("For how many years will the account earn interest? "))

#Formula
#fAnnual_Interest/iCompounding = interest rate per compounding period
#1 = interest for one period
#iCompounding*fPeriods = the total amount of times the interest will compound upon itself, resulting in the exponential value
#fStarting_Principal multiplied by the compounding factor produced by the other operations in the formula

fCompound_Interest = fStarting_Principal * ((1+(fAnnual_Interest/iCompounding))**(iCompounding*fPeriods))

#added if/else statements to convert the fPeriod to an integer to drop the decimal if it is a whole number
#if the fPeriod entered is decimal, it will keep the decimal to represent a portion of the year

fTime = fPeriods
if fTime == int(fTime):
    fTime = (int(fTime))
else:
    fTime = (fTime)

#output displays total of account (principal & interest) after the specified number of periods has passed
#formatted to display two decimal points

print("At the end of ", fTime, "years you will have $ " + format(fCompound_Interest,'.2f'))
