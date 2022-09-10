
#FILENAME binsearch.py
# First Last Stacy Goldstein
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: the summer work on binary searches 

import random
#generate random list of 20 numbers 
data=[]
n=20
for i in range(n):
    data.append(random.randint(1,100))
print("20 Random Numbers *not sorted* : " + str(data))

#sort data in increasing order 
data.sort()

print("Sorted list:" + str(data))

#binarySearch

low = 0 #setting low index to 0
high = len(data) -1 #setting high to highest index of list 
mid = 0
while(low <=high):
  mid = (high + low)//2
  if data[mid] < 6:
    low = mid + 1
  elif data[mid] >6 :
    high = mid -1
  else:
    print("The number is found in the array")
    break

#print("The value is not found in the array")
