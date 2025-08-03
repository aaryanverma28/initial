# while loops

# qs1
i = 1
while i <= 100:
    print(i)
    i += 1

# qs2
i = 100
while i >= 1: #stopping condition
    print(i)
    i -= 1

# qs3
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(i)
    i+=1

# qs4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# qs5
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        i += 1

# for loops

nums = [1, 4, 9 , 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

nums = (1, 4, 9 , 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("found at idx", idx)
        break
    idx += 1

for i in range(1, 101): # range(start, stop)
    print(i)

# for & range()

for i in range(1, 101): # range(start, stop)
    print(i)

for i in range(100, 0  ,-1): 
    print(i)

n = int(input("Enter a number: "))

for i in range(1, 11): 
    print(n * i)

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum =", sum)

n = 4
fact = 1

for i in range(1, n + 1):
    fact *= i

    print("factorial =", fact)