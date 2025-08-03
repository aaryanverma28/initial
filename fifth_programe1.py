# for loops

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)


tup = (1, 2, 3, 4, 5)

for val in tup:
    print(val)


str = "verma enterprises"

for char in str:
    if (char == 's'):
        print("s found")
        break
    print(char)
else:
    print("END")

seq = range(10)

for val in seq:
    print(val)

for i in range(10): #range(stop)
    print(i)

for i in range(2,10): #range(start, stop)
    print(i)

for i in range(1, 100 , 2): #range(start, stop, step)
    print(i)

for i in range(5):
    pass

if i > 5:
    pass

print("some hard work")