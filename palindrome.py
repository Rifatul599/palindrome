number = int(input("enter a number :"))
temp=number
reverse=0
while(number>0):
    digit=number%10
    reverse=reverse*10+digit
    number=number//10

if temp==reverse :
    print("The number is palindrome")

else:
    print("The number is not palindrome")
