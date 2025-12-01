#Author: Katlyn Lucis     11/26/2025
#CIT-115-D02 Python Programming
#Real Estate Analyzer

#Defining the main function.
def main():

    #Create an empty list to hold the property values that will be input.
    RealEstateList = []
    #Commission rate supplied by the assignment.
    fCommissionRate = .03

    #Calls the getFloatInput function to return property sale values.
    #After the function is called, the returned value is added to the RealEstateList.
    fRealEstateValue = getFloatInput("Enter Property Sales Value: ")
    RealEstateList.append(fRealEstateValue)
    #A while loop is set to true to continue until ended with break.
    while True:

        #The loop begins when the user is asked if they wish to enter another value.
        sAgain = input("Enter another value Y or N: ")

        #If Y or y is entered, a new value will be obtained by calling the getFloatInput function again.
        #The new value is added to the end of the RealEstateList.
        if sAgain == "Y" or sAgain == "y":
            fRealEstateValue = getFloatInput("Enter Property Sales Value: ")
            RealEstateList.append(fRealEstateValue)
        #If N or n is entered, the loop will break and the program will continue.
        elif sAgain == "N" or sAgain == "n":
            break
        #If anything other than Y, y, N, or n is entered, the loop will restart and prompt for Y(y) or N(n).
        else:
             pass

    #The RealEstateList is sorted in ascending order.
    list.sort(RealEstateList)

    #getMedian function is called and returns the value for fMedian.
    fMedian = getMedian(RealEstateList)

    #All values are calculated and displayed with proper formatting based on the assignment example.
    #A for loop is initiated based on how many items were added to the list.
    for iProperty in range(len(RealEstateList)):
        #The value of iProperty is added to 1 so the value of 0 does not show.
        #The loop continues for as many items as were entered, displaying the index number +1, and the value.
        print("Property ", str(iProperty+1), "$", format((RealEstateList[iProperty]),'11,.2f'))
    #The minimum of the list is printed using the min summary function.
    print("Minimum:     $", format(min(RealEstateList),'12,.2f'))
    #The maximum of the list is printed using the max summary function.
    print("Maximum:     $", format(max(RealEstateList),'12,.2f'))
    #The total of the list is printed using the sum summary function.
    print("Total:       $", format(sum(RealEstateList),'12,.2f'))
    #The average of the list is printed using the sum() divided by the length of the list.
    print("Average:     $", format((sum(RealEstateList)/len(RealEstateList)),'12,.2f'))
    #The fMedian formatted and printed to display the median.
    print("Median:      $", format(fMedian,'12,.2f'))
    #The commission total is found by multiplying the sum() of the list by the commission rate.
    print("Commission:  $", format((sum(RealEstateList)*fCommissionRate),'11,.2f'))
    
#Define the getFloatInput function.
def getFloatInput (fQuery):
    fQueryValue = 0
    #Data validation loop performed for value input.
    while fQueryValue <=0:
        try:
            fQueryValue = float(input(fQuery))
            #If the value is less than or equal to 0, a prompt will display.
            if fQueryValue <= 0:
                print("Input a number that is greater than 0.")
        #Exception added for non-numeric values.
        except ValueError:
            print("Input a number that is greater than 0.")
    #Value returned to the main function at the end of the validation.
    return fQueryValue

#Define getMedian function.
#List is passed to the function.
def getMedian (List):
    #The function tests if the length of the list is even or odd.
    #If the list is divisible by 2 with no remainder, it is deemed even.
    #An even number will require both of the middle most indices be found.
    if (len(List) % 2) == 0:
        #The index of the second middle value is found with integer division.
        iIndexEnd = len(List)//2
        #The index of the first middle value is found by subtracting one from the integer division result.
        iIndexStart = len(List)//2-1
        #fMedian is determined by adding the values at each index in the list and dividing the total by 2.
        fMedian = ((List[iIndexStart]+List[iIndexEnd])/2)
    #If the list is found to be odd, the follow else executes.
    else:
        #The index of the middle number is found using integer division.
        iIndex = len(List)//2
        #The property value at fIndex is assigned to fMedian.
        fMedian = List[iIndex]
    #fMedian is returned to the main function.
    return fMedian
        
#Call the main function.
main()
