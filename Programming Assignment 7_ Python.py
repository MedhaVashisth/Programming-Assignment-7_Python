#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python 3 code to find sum
# of elements in given array


def _sum(arr):

	# initialize a variable
	# to store the sum
	# while iterating through
	# the array later
	sum = 0

	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i

	return(sum)


# driver function
arr = []
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print('Sum of the array is ', ans)


# In[2]:


# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest(arr, n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

# This code is contributed by Smitha Dinesh Semwal


# In[3]:


# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))

# this code is contributed by Anabhra Tyagi


# In[5]:


# Python program to split array and move first
# part to end.

def splitArr(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x
		

# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
	print(arr[i], end = ' ')

# Code Contributed by Mohit Gupta_OMG <(0_o)>


# In[6]:


# Python Program to check if given array is Monotonic

# Check if given array is Monotonic


def isMonotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
			all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))

# This code is written by
# Sanjit_Prasad

