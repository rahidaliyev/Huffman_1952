from arrayInput import InputArrayPredefined 
from calculateToRightDirection import CalculateRightDirection
# arr = list()
# num = input("Enter length of array: ")
# sum = 0

arr = []
num = 13 
sum = 0
InputArrayPredefined(arr,num,sum)
arr.sort(reverse=True)
CalculateRightDirection(arr)
