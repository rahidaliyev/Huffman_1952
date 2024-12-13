from arrayInput import InputArray 
from calculateToRightDirection import CalculateRightDirection
arr = list()
num = input("Enter length of array: ")
sum = 0
InputArray(arr,num,sum)
arr.sort(reverse=True)
CalculateRightDirection(arr)
