#############################################################################
#ArmStrong_Number
'''

n="153"
d=int(n)
c=0
for i in n:
    c=c+(int(i)*int(i)*int(i))

print(c)

if d==c:
    print("Its a Armstrong No")
else:
   print("Not Armstrong No")

'''
########################################################################################
'''
a=153
arm_no=0
while a>0:
    c=a%10
    arm_no=(c**3)+arm_no
    a=a//10
print(arm_no)
'''
########################################################################################

'''
l=[56,87,1596,486]

max=l[0]

for i in l:
    if max<=i:
        max=i
print(max)

min=l[0]
for i in l:
    if min>=i:
        min=i
print(min)
'''
#################################################################################################

'''
l1=[1,2,3,4,5,6,7,8,9,10]

squares=[no*no for no in l1 ]
print(squares)

evens=[e for e in l1 if e%2==0]
print(evens)

odds=[o for o in l1 if o%2!=0]
print(odds)

evenodd=["EVEN" if e%2==0 else "ODD" for e in l1]
print(evenodd)


marks=[45,85,97,78,45]
new_marks=[m+5 for m in marks]
print(new_marks)
##############################################################################################

#DICT

evenodddd={y:"Even" if y%2==0 else "ODD" for y in l1}
print(evenodddd)

##########################################################################3


newev_odd=[no for no in l1 if no%2==0 if no%4==0]
print(newev_odd)
'''
######################################################################3#############################
'''
for i in range(5):
    #print("nelson")
    if i==6:
       print(i)
       break
else:
    print("After a for loop")
'''
###############################################

