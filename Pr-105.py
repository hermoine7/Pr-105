import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData1 = list(reader)

fileData=fileData1[0]
totalData=0
dataLenght=len(fileData)
squaredList=[]
sumOfList=0

for line in fileData:
    totalData += int(line)

mean=totalData/dataLenght

for value in fileData:
    newValue=int(value)-mean
    newValue=newValue**2
    squaredList.append(newValue)

for value in squaredList:
    sumOfList+=value

result= sumOfList/dataLenght

standardDeviation= math.sqrt(result)

print("Standard Deviation is: ", standardDeviation)