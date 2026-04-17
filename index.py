# # a="drisya"
# # print(a)
# # x = 20
# # print(x)
# # y = 19.6
# # print(y)
# # z=[1,2.5,2]
# # print(z)
# # print(z[0])
# # print(z[-1])
# # z.append(5)
# # print(z)
# # z.insert(0,8)
# # print(z)
# # z.pop()
# # print(z)
# # z.pop(2)
# # print(z)
# # p=(25,36,8)
# # print(p)
# # q=("ammu","varadha","midhu")
# # r=list(q)
# # r.append(5)
# # q=tuple(r)
# # print(q)

# # #user input

# # #name = int(input("enter your age:"))
# # #print(type(name))

# # #Check if a number is positive or negative.

# # a = int(input("enter a number"))
# # if a>=0:
# #     print("number is positive")
# # else:
# #     print("number is negetive") 

# # #Check whether a number is even or odd.       

# # b= int(input("enter a number"))
# # if(b%2==0):
# #     print("even")
# # else:
# #     print("odd")  

# # #Check if a person is eligible to vote (age ≥ 18).

# # age = int(input("enter a number"))
# # if age >=18:
# #     print("eligible for vote")
# # else:
# #     print("not elegible for vote")

# # #Check whether a number is divisible by 5.

# # num = int(input("enter a number"))
# # if num%5 == 0:
# #     print("divisible by 5")
# # else:
# #     print("not divisible by 5")

# # #Check if a character is a vowel or consonant.

# # c = input("enter a character")
# # if c in "aeiou":
# #     print("vowels")
# # else:
# #     print("consonent")

# # #Write a program to check if a number is zero, positive, or negative.

# # num = int(input("enter a number"))
# # if num>0 :
# #     print("positive")
# # elif num<0:
# #     print("negetive")
# # else:
# #     print("zero")

# # #Check whether a number is a multiple of 3 and 7.

# # x = int(input("enter a number"))
# # if x%3 == 0 and x%7 == 0:
# #     print("multiple of 3 and 7")
# # else:
# #     print("not a multiple 3 and 7")

# # #Take a password input and check if it matches a predefined password.       
       
# # letter = input("enter a password")
# # if letter =='drisyaaa12':
# #     print("match")
# # else:
# #     print("mismatch")    

# #Check whether a year is a leap year or not.

# # y = int(input("enter a year"))
# # if (y%4==0 and y%100!=0) or (y%400==0):
# #     print("leap year")
# # else:
# #     print("not a leap year")    

# # Simple calculator using if-elif (add, subtract, multiply, divide).

# num1 =int(input("enter the first number"))
# num2 =int(input("enter the second number"))
# p = input("enter operator (+,-,*,/)")
# if p =="+":
#     print("num1 + num2")
# elif p =="-":
#     print("num1-num2")
# elif p =="*":
#     print("num1*num2")
# elif p =="/":
#     print("num1/num2")
# else:
#     print("error")

# check a number is divisible by 2 and 5

# x = int(input("enter a number"))
# if x%2 == 0 and x&5 ==0:
#     print("number is divisible by 2 and 5")
# else:
#     print("nuber is not divisible by 2 and 5")    

# Check whether a number lies between 1 and 100.

# z = int(input("enter a number"))
# if 1<z<100:
#     print("it is lies between 1 and 100")
# else:
#     print("it is not lies between 1 and 100") 

#find the smallest among 3 numbers

# x = int(input("enter thr first number"))
# y = int(input("enter the second number"))
# z = int(input("entr the third number"))
# if y>x<z:
#     print("x is the smallest number")
# elif x>y<z:
#     print("y is the smallest number")
# else:
#     print("z is the smallest number")

#ATM Withdrawal (check balance before withdrawal)
        
# balance = 10000
# amount = int(input("enter the amount"))
# if amount>balance:
#     print("insufficient bank balance")
# elif amount<0:
#     print("amount should be positive")
# else:
#     new = balance-amount
#     print("bank balance is",new)        

# Movie ticket pricing:Child(<12)=


 


       

    






          # for loops

# print numbers from 1 to 10

# n=11
# for i in range(1,n):
#     print(i)

# print all even numbers from 1 to 20

# for i in range(1,21):
#     if i%2==0:
#         print(i)

# print all odd eveen numbers from 1 to 20

# for i in range(1,21):
#      if i%2!=0:
#          print(i)

# print multiplication table of a number

# n=2
# for i in range(1,11):
#     m=n*i
#     print(i) 

# print numbers in reverse (10 to 1)

# for i in range (10,0,-1):
#     print(i)

# print sum of numbers from to n

# n=21
# sum = 0
# for i in range (1,n+1):
#     sum += i
#     print(sum)

# print square of numbers from 1 to 10.
# for i in range(1,11):
#     m=i**2
#     print(m)

        #while loops

# print numbers from 1 to 10
# i=1
# while i<=10:
#     print(i)
#     i+=1

# print all even numbers from 1 to 20  

# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1

#  print all odd numbers from 1 to 20 

# i=1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     i+=1 

#  print multiplication table of a number 

# num=4
# i=1
# while i<=10:
#     mult=num*i
#     print(mult)
#     i+=1

# print numbers in reverse (10 to 1)

# i=10
# while i>=1:
#     print(i)
#     i-=1

# print sum of numbers from to n

# n=10
# sum = 0
# i=1
# while i<=10:
#     sum +=i
#     i+=1
#     print(sum)

#  print square of numbers from 1 to 10

# i=1
# while i<=10:
#     m=i**2
#     print(m)
#     i+=1
     
                #functions

# def  fun():
#     print("my name is Drisya")
# fun()    

# def fun(a,b):
#     print(a+b)
# fun(20,10)  
 

# Student Name List Create a list of at least 5 student names. Use a loop to print each name with a friendly greeting.

student=["midhu","varu","nandha","aami","samu","akku"]
for name in student:
    print("Helloo",name,"how are you...?")





    
    