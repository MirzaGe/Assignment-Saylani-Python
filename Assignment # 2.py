#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program which takes 5 inputs from user for different subject’s
#marks, total it and generate mark sheet using grades ?


# In[5]:


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[ ]:


#Write a program which take input from user and identify that the given
#number is even or odd?


# In[ ]:


# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.


# In[6]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[ ]:





# In[ ]:


#Write a program which print the length of the list?


# In[7]:


# Python code to demonstrate 
# length of list 
# using naive method 

# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ] 

# Printing test_list 
print ("The list is : " + str(test_list)) 

# Finding length of list 
# using loop 
# Initializing counter 
counter = 0
for i in test_list: 
	
	# incrementing counter 
	counter = counter + 1

# Printing length of list 
print ("Length of list using naive method is : " + str(counter)) 


# In[ ]:





# In[ ]:


#Write a Python program to sum all the numeric items in a list?


# In[8]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[ ]:





# In[ ]:


#Write a Python program to get the largest number from a numeric list.


# In[9]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))


# In[ ]:





# In[ ]:


#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are
#less than 5.


# In[20]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

        print(i)


# In[ ]:





# In[ ]:




