#importing the json library
import json
#importing the get_close_matches from difflib library
from difflib import get_close_matches

#opening the data.json file and loading it into a variable called dataSet with the help of json module.
dataSet = json.load(open("data.json"))

#2-after prompting the user at 1, the input user has typed
# is sent into this function as an input.
def meaningOf(thisWord):
    #conerting the input to lower case and store in a variable called con.
    con = thisWord.lower()
    #check if the variable value of con is present in the dataSet
    if con in dataSet:
        #if above condition is true, return the value of dataSet[con] (con is a key,so it returns the value of con)
        return dataSet[con]
    #first converts the inputs first letter to uppercase and checks if its present in dataSet.
    elif thisWord.title() in dataSet:
        #if above condition is True,this returns the value of dataSet[con] (con is a key,so it returns the value of con)
        return dataSet[thisWord.title()]
    # first converts the input uppercase and checks if its present in dataSet.
    elif thisWord.upper() in dataSet:
        # if above condition is True,this returns the value of dataSet[con] (con is a key,so it returns the value of con)
        return dataSet[thisWord.upper()]

    #get_close_matches will take two parameters,
    # here,it takes the word user has typed and the other parameter which takes the list of keys present in dataset
    #it compares the input with those keys and returns them which are nearly same.
    #but the condition we did here, check if the length of returned keys is greater than 0
    #it means we know that one/some keys exist and condition will be true and inside code will be executed.
    elif len(get_close_matches(con, dataSet.keys())) > 0:
        #prompt the user to confirm with the word/key that has been returned by get_close_matches
        #prompt the user to type Y for yes and N for no
        #and the get_close_matches returns the matched keys in order,that is
        #the most close match is kept at the first of its order so we use only that first match to show to user
        #we use dataSet.keys())[0] for that
        yORn = input('Did you mean {} ?.\nType "Y" for yes or "N" for not.\n '.format(get_close_matches(con, dataSet.keys())[0]))
        #if user types Y then code inside gets executed
        if yORn == "Y":
            #returns the value/meaning of closest match found for the key
            # that user accepted to know the meaning of get_close_match,when user is prompted to type y or n.
            return dataSet[get_close_matches(con, dataSet.keys())[0]]
        # if user types N then code inside gets executed
        elif yORn == "N":
            # returns the below sentence
            return "Please re-check the word you have typed!"
        #if user types anything other than Y or N
        else:
            return "Only 'Y' or 'N ' are allowed!"
    #if the word dosnt exist in dataSet or fails in all the conditions above then
    # the below will be returned
    else:
        return "Word doesnt exist!"

#1-prompt the user to enter the word and then convert it
# into a string and store it in a variable called toFind.
toFind = str(input("Enter any word :"))
#send the value in toFind variable as input parameter of
# meaningOf() function and what ever will be returned by
# that function will be stored in returnedValue.
returnedValue =meaningOf(toFind)
#check if the returnedValue is of type list .
if type(returnedValue) == list:
    #from the returnedValue print every listItem in it.
    for listItem in returnedValue:
        print(listItem)
#if the returnedValue is not a list, print what ever the value returnedValue has.
else:
    print(returnedValue)
