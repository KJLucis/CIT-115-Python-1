#Author: Katlyn Lucis     11/18/2025
#CIT-115-D02 Python Programming
#Paint Job Calculator

#Begin by importing the math module as it will be needed later to use the ceiling function.
import math


#Defining the main function.
def main():

#Calling getFloatInput function, the user is prompted to enter the requested information.
    fSqFtWall = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFtPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHourPerGallon = getFloatInput("How many labor hours per gallon: ")
    fPaintingLaborPerHour = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")

#Calls all the functions to perform calculations and find the remaining variables required.
#Variables are returned at the end of their respective functions to be called for future use.
#getGallonsOfPaint passes the square feet of the wall and feet per gallon to return the total gallons.
    iTotalGallons = getGallonsOfPaint(fSqFtWall,fFtPerGallon)
#getLaborHours passes the labor hours per gallon and total gallons as arguments to return the value of fLaborHours
    fLaborHours = getLaborHours (fLaborHourPerGallon,iTotalGallons)
#getPaintCost passes the price of the paint and the total gallons as arguments to return the total cost of paint.
    fPaintCost = getPaintCost (fPaintPrice,iTotalGallons)
#getLaborCost passes the cost of labor per hour and the labor hours required to return the total cost of labor.
    fLaborCost = getLaborCost (fPaintingLaborPerHour,fLaborHours)
#getSalesTax passes the state as an argument to it's function to return the sales tax.
#The labor and paint costs already returned are multiplied by the sales tax.
    fSalesTax = (getSalesTax (sState))*(fLaborCost+fPaintCost)
#showCostEstimate calculates the total cost, and prints the calculated variables.
    fCostEstimate = showCostEstimate (iTotalGallons,fLaborHours,fPaintCost,fLaborCost,fSalesTax)
#Final function is called to create an output based on what was printed during showCostEstimate
    writeOutput(sLastName,iTotalGallons,fLaborHours,fPaintCost,fLaborCost,fSalesTax,fCostEstimate)


#Define the getFloatInput function.      
#Data validation loop performed for value input.
#Exception added for non-numeric values
#Value returned to the main function at the end of the validation.
def getFloatInput (fQuery):
    fQueryValue = 0
    while fQueryValue <=0:
        try:
            fQueryValue = float(input(fQuery))
            if fQueryValue <= 0:
                print("Input must be a positive numeric value")
        except ValueError:
            print("Input must be a positive numeric value")
    return fQueryValue


#Define getGallonsOfPaint function.
#Wall area divided by area one gallon of paint covers to find total gallons needed.
#Function uses the math module ceiling function to round the gallon amount up to a whole number.
#The value is returned after being converted to an int.
def getGallonsOfPaint (fSqFtWall,fFtPerGallon):
    iTotalGallons = math.ceil(fSqFtWall/fFtPerGallon)
    return int(iTotalGallons)


#Define getLaborHours function.
#Amount of time needed to use one gallon multiplied by the number of total gallons required.
#Total hours needed to complete the job returned as a float.
def getLaborHours(fLaborHourPerGallon,iGallons):
    fLaborHours = fLaborHourPerGallon*iGallons
    return float(fLaborHours)


#Define getLaborCost function.
#The cost of each labor hour is multiplied by how many hours will be required.
#The total cost of labor is returned as a float.
def getLaborCost (fPaintLaborPerHour,fLaborHours):
    fLaborCost = fPaintLaborPerHour*fLaborHours
    return float(fLaborCost)


#Define getPaintCost function.
#The price of each gallon of paint is multiplied by the number of total gallons required.
#The total cost of the paint is returned as a float.
def getPaintCost (fPaintPrice,iGallons):
    fPaintCost = fPaintPrice*iGallons
    return float(fPaintCost)


#Define getSalesTax function.
#The string received from the main function is tested in a sequence of if/elif/else statements.
#Based on which state was input, the appropriate sales tax will be returned as a float.
def getSalesTax (sState):
    if sState == "CT" or sState == "ct":
        fSalesTax = .06
    elif sState == "MA" or sState == "ma":
        fSalesTax = .0625
    elif sState == "ME" or sState == "me":
        fSalesTax = .085
    elif sState == "NH" or sState == "nh":
        fSalesTax = .0
    elif sState == "RI" or sState == "ri":
        fSalesTax = .07
    elif sState == "VT" or sState == "vt":
        fSalesTax = .06
    else:
        fSalesTax = 0   
    return float(fSalesTax)


#Define showCostEstimate function.
#Total cost of project is evaluated by adding the total cost of paint, labor, and sales tax together.
#The final summary of various costs are printed with proper formatting.
#The total cost of the project is returned for use in the last function.
def showCostEstimate (iGallons,fLaborHours,fPaintCost,fLaborCost,fSalesTax):
    fCostEstimate = fPaintCost+fLaborCost+fSalesTax
    print("Gallons of paint: ", (iGallons))
    print("Hours of Labor: ", (fLaborHours))
    print("Paint charges: $"+ format(fPaintCost, '.2f'))
    print("Labor charges: $"+ format(fLaborCost, '.2f'))
    print("Tax: $" + format(fSalesTax, '.2f'))
    print("Total Cost: $"+ format(fCostEstimate,'.2f'))
    return fCostEstimate


#Defines the writeOutput function.
#Creates a new file named the value that was input for last name, followed by _PaintJobOutput.txt.
#The previous print outputs are written to the file, with \n creating a new line.
#The newly created file is closed.
#A prompt that the file was created is printed with the file name.
def writeOutput (sName,iGallons,fLaborHours,fPaintCost,fLaborCost,fSalesTax,fTotalCost):
    Job_File = open(f'{sName}_PaintJobOutput.txt', 'w')
    Job_File.write(f'Gallons of paint: {iGallons}\n')
    Job_File.write(f'Hours of Labor: {fLaborHours}\n')
    Job_File.write(f'Paint charges: ${fPaintCost:.2f}\n')
    Job_File.write(f'Labor charges: ${fLaborCost:.2f}\n')
    Job_File.write(f'Tax: ${fSalesTax:.2f}\n')
    Job_File.write(f'Total Cost: ${fTotalCost:.2f}\n')
    Job_File.close()
    print(f'File: {sName}_PaintJobOutput.txt was created.') 

#Call the main function
main()
