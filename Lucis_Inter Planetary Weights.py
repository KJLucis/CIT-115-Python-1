#Author: Katlyn Lucis    9_10_2025
#CIT-115-D02 Python Programming
#Inter Planetary Weights

#Planetary Constants
#specific gravity factors for each planet to be used in formula, converted to float
#represent respective planet's gravity compared to Earth's per 1 lb
#factors provided by assignment

fMERCURY_GRAVITY = float(0.38)
fVENUS_GRAVITY = float(0.91)
fMOON_GRAVITY = float(0.165)
fMARS_GRAVITY = float(0.38)
fJUPITER_GRAVITY = float(2.34)
fSATURN_GRAVITY = float(0.93)
fURANUS_GRAVITY = float(0.92)
fNEPTUNE_GRAVITY = float(1.12)
fPLUTO_GRAVITY = float(0.066)

#User Inputs string Name and float Weight to be used in the below formula and print functions

sName = input("What is your name: ")
fWeight = float(input("What is your weight: "))

#Formula: planet weight = planet gravity factor * earth weight
#factors pulled from constants, multiplied by the weight input by user

fMercury_Weight = fMERCURY_GRAVITY*fWeight
fVenus_Weight = fVENUS_GRAVITY*fWeight
fMoon_Weight = fMOON_GRAVITY*fWeight
fMars_Weight = fMARS_GRAVITY*fWeight
fJupiter_Weight = fJUPITER_GRAVITY*fWeight
fSaturn_Weight = fSATURN_GRAVITY*fWeight
fUranus_Weight = fURANUS_GRAVITY*fWeight
fNeptune_Weight = fNEPTUNE_GRAVITY*fWeight
fPluto_Weight = fPLUTO_GRAVITY*fWeight

#Results of the formula for each specific planet printed, in float.
#print function formatted to take the first 25 positions on the left side
#10.2 represents outputted weight taking 10 positions with 2 decimal points
#f converts the planet_weight back into a floating number instead of scientific notation.

print(sName + " here are your weights on our Solar System's planets:")
print(format("Weight on Mercury:", "25s") + format(fMercury_Weight,'10.2f'))
print(format("Weight on Venus:", "25s") + format(fVenus_Weight,'10.2f'))
print(format("Weight on our moon:", "25s") + format(fMoon_Weight,'10.2f'))
print(format("Weight on Mars:", "25s") + format(fMars_Weight,'10.2f'))
print(format("Weight on Jupiter:", "25s") + format(fJupiter_Weight,'10.2f'))
print(format("Weight on Saturn:", "25s") + format(fSaturn_Weight,'10.2f'))
print(format("Weight on Uranus:", "25s") + format(fUranus_Weight,'10.2f'))
print(format("Weight on Neptune:", "25s") + format(fNeptune_Weight,'10.2f'))
print(format("Weight on Pluto:", "25s") + format(fPluto_Weight,'10.2f'))
