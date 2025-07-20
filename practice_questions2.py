name = input("enter your name: ")
print("length of your name is: ", len(name))

str = " Hey $Iam the $ symbol $999.999"
print(str. count("$"))

num = int(input("enter a number: "))

if(num % 2 == 0):
    print("even")
else:
    print("odd")

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a > b and a > c):
    print("first number is largest", a)
elif(b > a and b > c):
    print("second number is largest", b)
else:
    print("third number is largest", c)

x = int(input("enter number: "))

if(x % 6 == 0):
    print("multiply of 6")
else:
    print("not a multiply")