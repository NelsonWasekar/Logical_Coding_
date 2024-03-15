

#Armstrong number is a number that is equal to the sum of cubes of its digits.

# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.


#b=153

###########################################################3

# Using While loop

'''
n=int(input("ENter a number :"))
b=n
sum=0
while n>0:
    y=n%10
    sum=(y**3)+sum
    n=n//10

if b==sum:
    print("Its Armstrong Number")
else:
    print("Its not an Armstrong Number")
'''
##############################################################################################
#Using String

a=input("Enter a number :")
d=0

for i in a:
    d=d+(int(i)*int(i)*int(i))
    print(d)

c=int(a)
if c==d:
    print("Its a Armstrong Number")
else:
    print("Its not a Armstrong Number")

###############################################################################################
