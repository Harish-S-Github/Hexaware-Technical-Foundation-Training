a=13
b=5
c=7
if a>b and a>c:
    print("a is the greatest")
elif b>c:
    print("b  is the greatest")
else:
    print("c is the greatest")

1) Write a Python program that takes an integer input from the user and prints "Positive" if the number is greater than 0.
a=int(input("Enter a number: "))
if(a>0):
    print(a," is positive")
else:
    print(a, " is negative")


2) Given a variable temperature, write an if statement that prints "Hot day!" if temperature is greater than 30.
temperature = int(input("Enter a number: "))
if(temperature>30):
    print("Hot")
else:
     print("cold")


3) Write a program that asks the user to enter a number and checks if it is even. If it is, print "Even number".
4) Write a Python program that checks if a number is even or odd. Print "Even" if it is even, otherwise print "Odd".
num=int(input("enter a num "))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")


5)Write a program that asks the user to enter their age. If they are 18 or older, print "Eligible to vote", otherwise print "Not eligible to vote".
age=int(input("enter your age "))
if(age>18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

6)Create a program that asks the user to enter a password. If the password is "admin123", print "Access Granted", otherwise print "Access Denied"
password=input("enter your password:")
if(password=="admin123"):
    print("Access Granted")
else:
    print("Access Denied")

 Program 7: Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

Program 8: Grading System
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

 Program 9: Check if a Year is a Leap Year
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

 Program 10: Greeting Based on Time
time = int(input("Enter the current time (0-23): "))
if 5 <= time < 12:
    print("Good Morning")
elif 12 <= time < 17:
    print("Good Afternoon")
elif 17 <= time < 21:
    print("Good Evening")
else:
    print("Good Night")


for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


rows = int(input("Enter number of rows: "))
for i in range(rows):
     for j in range(i+1):
         print(j+1, end=" ")
     print()







 1) Reverse a list in Python
 lis=[1,3,5,7,9,11,13,17,19]
lis.reverse()
print(lis)

 2) Concatenate two lists index-wise
 4) Concatenate two lists in the following order
lis2=[2,4,6,8,10,12,14,16,18,20,"",""]
result = [item for pair in zip(lis, lis2) for item in pair]
 print(result)

3) Turn every item of a list into its square
for i in result:
    print(i*i)


 5) Iterate both lists simultaneously
for i in range(len(lis)):
    print(lis[i])
for j in range(len(lis2)):
        print(lis2[j])

 6) Remove empty strings from the list of strings
print(lis2)
while(""in lis2):
    lis2.remove("")
print(lis2)


 7) Exercise 7: Add new item to list after a specified item
lis.insert(0,0)
print(lis)

 8) Extend nested list by adding the sublist
sub=[21,23]
lis.extend(sub)
print(lis)

 9) Replace list’s item with new value if found
lis2[4]=12
print(lis2)


10) Remove all occurrences of a specific item from a list.

unique_list = []  

for item in lis2:  
    if item not in unique_list:  
        unique_list.append(item)  

print(unique_list)  
