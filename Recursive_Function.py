

#Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body.
# Usually, it is returning the return value of this function call.
# If a function definition fulfils the condition of recursion, we call this function a recursive function.

#n= int(input("Enter an in integer ="))
#Using a function

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

d=fact(5)
print(d)