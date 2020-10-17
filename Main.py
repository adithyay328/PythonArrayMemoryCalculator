sizeOfDataType = int(input("What is the size of the datatype? "))
numberofDimensions = int(input("How many dimensions are in the array? "))

#Setting it to size of data type so following for loop
#will return the right value after multiplying
#by the length of each dimension.
currentMemorySize = sizeOfDataType

#Find the correct memory size by finding product of currentMemorySize
#and the lenght of each dimension.
for i in range(1, numberofDimensions + 1):
    lengthOfCurrentDimension = int(input("What is the length of dimension #" + str(i) + "? "))
    currentMemorySize *= lengthOfCurrentDimension

print("Size of the array in memory: " + str(currentMemorySize))