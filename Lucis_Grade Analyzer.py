#Author: Katlyn Lucis   9_26_2025
#CIT-115-D02 Python Programming
#Grade Analyzer

#User inputs name, as well as 4 test scores all converted to integer.
sName = input("Name of person that we are calculating the grades for: ")

#All scores are assigned to an iTest variable
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

#User prompted if they wish to drop the lowest grade
sDrop = input("Do you wish to Drop the Lowest Grade Y or N? ")

#Program checks if any test score is less than 0
#If any scores are found to be less than 0, the program will shut down with SystemExit
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0")        
    raise SystemExit

#Program checks value of sDrop from the input received.
#If value was N for no, the fAverage will be calculated with all 4 scores, divided by 4.
if sDrop == "N":
    
    fAverage = (iTest1+iTest2+iTest3+iTest4)/4

#if the value of sDrop is Y for yes, a series of if/else will initiate to find which test score was the lowest.
#each test score is tested to see if it is greater than at least one other.  If it passes, it's value will be assigned
#to the corresponding iGrade.  If it fails to be greater than at least one other value, it will be assigned to it's
#corresponding iGrade at a value of 0.
elif sDrop == "Y":
    
    if iTest1 > iTest2 or iTest1 > iTest3 or iTest1 > iTest4:
        iGrade1 = iTest1
    else:
        iGrade1 = iTest1 = 0
        
    if iTest2 > iTest1 or iTest2 > iTest3 or iTest2 > iTest4:
        iGrade2 = iTest2
    else:
        iGrade2 = iTest2 = 0
        
    if iTest3 > iTest1 or iTest3 > iTest2 or iTest3 > iTest4:
        iGrade3 = iTest3 
    else:
        iGrade3 = iTest3 = 0
        
    if iTest4 > iTest1 or iTest4 > iTest2 or iTest4 > iTest3:
        iGrade4 = iTest4
    else:
        iGrade4 = iTest4 = 0

#The average of the tests is found by dividing their total by 3.
#The lowest of the scores will now equal 0, which essentially removes (drops) the grade.
    fAverage = (iGrade1+iGrade2+iGrade3+iGrade4)/3

#If a letter other than Y or N is typed, the program will show this message, then close via SystemExit.
else:
    print ("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

#The sName variable is pulled from the beginning, and the fAverage from above is pulled and formatted to 1 decimal point.
print(f"{sName}'s test average is: " + format(fAverage,'.1f'))

#The fAverage is used to assign a value to the sLetter.
#sLetter assigned based on which if or elif statement it is valued under.
#Scaling values obtained via assignement.
if fAverage >= 97.0:
    sLetter = "A+"
elif fAverage <= 96.9 and fAverage >= 94.0:
    sLetter = "A"
elif fAverage <= 93.9 and fAverage >= 90.0:
    sLetter = "A-"
elif fAverage <= 89.9 and fAverage >= 87.0:
    sLetter = "B+"
elif fAverage <= 86.9 and fAverage >= 84.0:
    sLetter = "B"
elif fAverage <= 83.9 and fAverage >= 80.0:
    sLetter = "B-"
elif fAverage <= 79.9 and fAverage >= 77.0:
    sLetter = "C+"
elif fAverage <= 76.9 and fAverage >= 74.0:
    sLetter = "C"
elif fAverage <= 73.9 and fAverage >= 70.0:
    sLetter = "C-"
elif fAverage <= 69.9 and fAverage >= 67.0:
    sLetter = "D+"
elif fAverage <= 66.9 and fAverage >= 64.0:
    sLetter = "D"
elif fAverage <= 63.9 and fAverage >= 60.0:
    sLetter = "D-"
elif fAverage <= 59.9 and fAverage >= 0.0:
    sLetter = "F"

#Letter grade is printed after the sLetter is assigned from the above statements.    
print(f"Letter Grade for the test is: {sLetter}")
