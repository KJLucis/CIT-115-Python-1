#Author: Katlyn Lucis   9_23_2025
#CIT-115-D02 Python Programming
#Temperature Converter

print("Welcome to the temperature converter.")

#User promted to enter temperature, and the temp scale used (F,f,C,c)
fTemperature = float(input("Enter a temperature: "))
sScale = input("Is the temp F for Fahrenheit or C for Celsius? ")

#-Step 1-

#First line of logic checks to see if the input is F or f for fahrenheit.  If not, proceed to Step 2.
#Step 1.1- If F or f was entered, it proceeds to check the input for temperature against the value of 212.
#212 is a number supplied by the assignment to be the highest number allowed.
#Step 1.2- If the value inputed for temperature is less than or equal to 212, the equation for converting the input into celsius will proceed.

if sScale == "F" or sScale == "f":
    if fTemperature > 212:
        print("Temp can not be > 212.")
    elif fTemperature <= 212:
        fCelsius = (5.0/9) * (fTemperature - 32)
        print("The Celsius equivalent is: " + format(fCelsius,'.1f'))

#-Step 2-
        
#Program proceeds to check if C or c was entered.  If not, proceed to Step 3.
#Step 2.1- If C or c was entered, causing sScale = c or C to be true, the input temperature will be checked against 100.
#100 is a number supplied by the assignment to be the highest number input allowed.
#Step 2.2- If the number is less than or equal 100, the equation will convert the input value into fahrenheit.

elif sScale == "C" or sScale == "c":
    if fTemperature > 100:
        print("Temp can not be > 100")
    elif fTemperature <= 100:
        fFahrenheit = ((9.0/5.0)*fTemperature) + 32
        print("The Fahrenheit equivalent is: " + format(fFahrenheit,'.1f'))

#-Step 3-
        
#If the input for sScale is no F,f,C, or c, the program will print this error and end.

else:
    print("You must enter a F or C")
        
