n=int(input("enter number:"))
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(n==rev):
    print("num is palindrome")
else:
    print("num is not palindrome")