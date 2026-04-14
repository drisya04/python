a="drisya"
print(a)
x = 20
print(x)
y = 19.6
print(y)
z=[1,2.5,2]
print(z)
print(z[0])
print(z[-1])
z.append(5)
print(z)
z.insert(0,8)
print(z)
z.pop()
print(z)
z.pop(2)
print(z)
p=(25,36,8)
print(p)
q=("ammu","varadha","midhu")
r=list(q)
r.append(5)
q=tuple(r)
print(q)

#user input

#name = int(input("enter your age:"))
#print(type(name))

#Check if a number is positive or negative.

a = int(input("enter a number"))
if a>=0:
    print("number is positive")
else:
    print("number is negetive") 

#Check whether a number is even or odd.       

b= int(input("enter a number"))
if(b%2==0):
    print("even")
else:
    print("odd")  

#Check if a person is eligible to vote (age ≥ 18).

age = int(input("enter a number"))
if age >=18:
    print("eligible for vote")
else:
    print("not elegible for vote")

#Check whether a number is divisible by 5.

num = int(int("enter a number"))
if num%5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

#
    
