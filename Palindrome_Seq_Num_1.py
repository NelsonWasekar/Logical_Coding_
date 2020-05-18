

y = input("Enter a sequence or number :")
x = y[-1::-1]
if x == y:
    print("Palindrome")
else:
    print("Not a palindrome")