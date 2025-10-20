#Author: Katlyn Lucis   10/16/2025 
#CIT-115-D02 Python Programming
#Compound Interest with Loops

#Obtain user input for variables.
#fStarting_Principal = initial amount of money in the account for which interest will be accrued upon
#fInterest_Rate = interest rate given as a % amount, then divided by 100 to give the required decimal amount
#iMonths = How many months the user would like to see the results compounded
#fGoal = What is the desired amount to accrue

#Begin by setting fStarting_Principal to 0 so the while loop will function.
fStarting_Principal = 0

#Since fStarting_Principal is 0, the while loop will begin.
#The "if" validates that the number is greater than zero, while the "except" ensures that the variable is a numeric value.
#This loop will excecute until it has successfully changed the value of fStarting_Principal to a positive numeric value.
while fStarting_Principal <= 0:
    try:
        fStarting_Principal = float(input("What is the Original Deposit (positive value): "))
        if fStarting_Principal <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")
    
    
fInterest_Rate = 0

#Since fInterest_Rate is 0, the while loop will begin.
#The "if" validates that the number is greater than zero, while the "except" ensures that the variable is a numeric value.
#This loop will excecute until it has successfully changed the value of fInterest_Rate to a positive numeric value.
while fInterest_Rate <= 0:
    try:
        fInterest_Rate = float(input("What is the Interest Rate (positive value): "))/100
        if fInterest_Rate <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

#Next, the interest rate value is divided by 12 to obtain the monthly interest rate.
fInterest_Rate /= 12

iMonths = 0

#Since iMonths is 0, the while loop will begin.  
#The "if" validates that the number is greater than zero, while the "except" ensures that the variable is a numeric value.
#This loop will excecute until it has successfully changed the value of iMonths to a positive numeric value.
while iMonths <= 0:
    try:
        iMonths = int(input("What is the Number of Months: "))
        if iMonths <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

fGoal = -1

#Since fGoal is -1, the while loop will begin.
#The "if" validates that the number is greater than or equal to zero, while the "except" ensures that the variable is a numeric value.
#This loop will excecute until it has successfully changed the value of fGoal to a positive numeric value or 0.
while fGoal < 0:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print("Input must 0 or greater")
    except ValueError:
        print("Input must be 0 or greater")

#iTime is added to track how many months the accrual will happen for.        
iTime=0

#iTime is set to zero for the following loop to continue until it is equal to the integer amount entered for iMonths.
#Each time the loop completes, 1 will be added to iTime.  This will display as the month number.
#Formula for fCompound_Interest supplied by assignment.
#The compounded interest will be calculated and displayed, and will continue to do so until the iMonths amount is reached.
while iTime < iMonths:

    iTime +=1
    fCompound_Interest = fStarting_Principal * ((1+(fInterest_Rate))**(iTime))
    print("Month: ", iTime, "Account Balance is: $ " + format(fCompound_Interest,'.2f'))

#to find the amount of months it will take for fGoal to be reached, iTime is reset to 0.
#in the event that fGoal was lower than fStarting_Principal, the calculation is run once at 0 months.
iTime=0
fCompound_Interest = fStarting_Principal * ((1+(fInterest_Rate))**(iTime))

#next, the while loop will begin if fCompound_Interest is less than the fGoal amount.
#each time the loop completes, it will add 1 to the iTime counter, which will display the total number of months.
#The calculation runs until the fCompound_Interest exceeds or equals the fGoal amount.
while fCompound_Interest < fGoal:

    iTime +=1
    fCompound_Interest = fStarting_Principal * ((1+(fInterest_Rate))**(iTime))

#Once the fGoal amount is less than or equal to the fCompound_Interest amount,
#or if the fStarting Principal was greater than fGoal to begin with,
#the accrued iTime value will display how many months it would have taken (how many times the equation had to run)
#to achieve the value of fGoal as inputted at the beginning of the program.
print("It will take: ", iTime, " months to reach the goal of $" + format(fGoal,'.2f'))
