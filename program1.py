prince=input("enter a string:")
rev_prince=reversed(prince)
if list(prince)==list(rev_prince):
    print("its palindrome")
else:
    print("its not palindrome")
