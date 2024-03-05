#l = [1,2,3,4,5,6]

#print(l>5)
'''
l2=l

print(l is l2)
'''

'''
l2= []
for i in l:
    if i>=3:
        l2.append(i)
    else:
        print(i)

print(l2)
'''

#l2 = [1,2,3,4,5,6]

'''
i=17
while i<171:
    #if i%17==0:
        print(i)
        i=i+17
'''

'''
i=1
while i<101:
    if i%2==0:
        print(i)
    i=i+1 '''

'''
for i in range(0, 101):
    if i %2==0:
        print(i) '''

'''
l=[1,2,3,14,15,16,27,28,39,50]
print(len(l))

i=0
while i<len(l):
      print(l[i]**2, end =" ")
      print(i)
      i=i+1

for i in l:
    print(i**2, end =" ")'''

'''
l1 = [10, 20,87, 678,90,23]
print(10<=20)
max=l1[0]
for i in l1:
    if max<=i:
        max=i
print(max)'''


'''
slt=('sales, Nashik, 6Feb2023')
#for i in slt:
k=slt.split(',')
print(k[2])
'''

'''
l=[1,2,3,14,15,16,27,28,39,50]

k = ['Even' if i%2==0 else 'Odd' for i in l]
print(k)'''

'''
l1 = [10, 20,87, 678,90,2]

min=l1[0]
for i in l1:
    if min >=i:
        min=i
print(min)'''

##################################################333
'''
n=int(input("Enter a number ?? "))
a=0
b=1
print(a, b, end= " ")
for i in range(n-1):
    c=a+b
    print(c, end=" ")
    a=b
    b=c
'''
##################################################################################33
'''
a = '153'   # 1634  [ 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634 ]
d=0
for i in a:
    d = d+( int(i) * int(i) * int(i))
c = int(a)

if c ==d:
    print("Its an Armstrong")
else:
    print("Its not an Armstrong")
'''
##############################################################################################
'''
n = int(input('Enter a number : '))
r = n[::-1]
print(r)
'''
#########################################################################################33