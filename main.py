import pandas
import importexport
from collections import defaultdict
#Welcome to our Overhead CEO Project

#FUNCTIONS - add/remove Package functions must be able to alter data structure

#1)addPackage - Adds package, arguments (int packageID, int aisle, int bay) - returns success or error

def addPackage():
        #input information
        print("\n---Provide Information---")
        packageID = str(input("\nPlease enter 6 digit # of package ID: "))

        while (len(packageID) != 6): #user input validation - 6 digits
                 packageID = str(input("\n!!! Please enter 6 digit # of package ID: "))

        while (packageID.isdecimal() == False):
                packageID = str(input("\n!!! Numbers only !!! -> Please enter 6 digit # of package ID: "))

        packageID = int(packageID)

        aisle = str(input("\nPlease enter aisle #: "))
        bay = str(input("\nPlease enter bay #: "))
        quantity = int(input("\nPlease enter quantity of boxes: "))
        location = str(aisle + "-" + bay)

        #logic
        print("\n---Adding---")
        if packageID in dict: #if packageID already exists | append to list new location instance
                for x in range(quantity): #quantity method
                        dict[packageID].append(location)
        else:
                dict[packageID] = [location] #adds list with location as value to dictionary
                for y in range(quantity - 1): #quantity method
                        dict[packageID].append(location)

#2)removePackage - Removes package, arguments (int packageID, int aisle, int bay) - returns success or error

def remPackage():

        #input information
        packageID = int(input("\nPlease enter 6 digit # of package ID: "))
        while (packageID not in dict):
                packageID = int(input("\nPackageID does not exist - > Please enter another 6 digit # of package ID: "))
        aisle = str(input("\nPlease enter aisle #: "))
        bay = str(input("\nPlease enter bay #: "))
        quantity = int(input("\nPlease enter quantity of boxes: "))
        location = str(aisle + "-" + bay)

        #logic
        print("\n---REMOVING---")
        if packageID in dict: #if key is in dict
                if location in dict[packageID]: #if location is in list, remove from list
                        for z in range(quantity): #quantity method
                                try: #catches error for removing too many boxes...
                                        dict[packageID].remove(location)
                                except:
                                        pass
                        print("\n---Remove Successfull---")
                        if not dict[packageID]: #If list empty, remove key 
                                del dict[packageID]
                else: #location does not exist
                        pass
        else: #key does not exist
                print("\n!!!PackageID does not exist!!!")

#3)searchPackage - Searches package, arguments (int packageID) - returns all instances of that package ID in a table, ex: Aisle-Bay | Count

def searchPackage():
        #input information
        print("\n---Provide Information---")
        packageID = int(input("\nPlease enter 6 digit # of package ID: "))

        #logic
        print("\n---Searching---")
        if packageID in dict:
                locations = dict[packageID] #list values Aisle-Bay
                countDict = {}
                for i in locations:
                        if i in countDict:
                                countDict[i] += 1
                        else:
                                countDict[i] = 1
                print("\n--- SKU found at these locations --- ")
                print("   --- Location | Quantity --- \n")
                for place in countDict:
                        print(str(place) + " | " + str(countDict[place]))
        else:
                print("\n!!!Package Not Found!!!\n")
#4)showInventory - Shows entire inventory of products, preferably ordered. 

def showInventory():
        print("\n---Showing Inventory---\n")
        #print(dict)

        #or
        print("ID | Location | Quantity\n")
        for key in dict:
                        locations = dict[key] #list values Aisle-Bay
                        countDict = {}
                        for i in locations:
                                if i in countDict:
                                        countDict[i] += 1
                                else:
                                        countDict[i] = 1
                        for place in countDict:
                                print(str(key) + " | " + str(place) + " | " + str(countDict[place]))
        print("\n---End Of Inventory---\n")

#quantity, warning for illegal quantities 

#Main Area

#User Input While Loop - (Mainly used before we develop an UI) - gives options for functions 1-3. Must have input validation

#File Download, read entire csv file into data structure.

dict = importexport.csv_read()

userInput = -1 #sentinel value
print("\n\n--- Welcome To Overhead-CEO ---\n")
while(userInput != 5):
    print("\n--- Options ---\n")
    print("1: Add Package \n2: Remove Package\n3: Search Package\n4: Show Inventory\n5: Exit")
    userInput = int(input("\nPlease select the desired function: "))
    if userInput == 1: #addPackage
            addPackage()
    elif userInput == 2: #removePackage
            remPackage()
    elif userInput == 3: #searchesPackage
            searchPackage()
    elif userInput == 4: #prints Dict
            showInventory()
    
importexport.csv_write(dict)    
#csvFile = pandas.read_csv('shaq-nba-career-regular-season-stats-by-game.csv')
#print(csvFile)






#File Upload, writer entire data structure to csv file.  

#END PROGRAM
