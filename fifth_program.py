count = 1
while count <= 5:
    print("Hello World")
    count += 1
    
i = 1       # i is a iterater
while i <= 100000:
    print("Aaryan", i)      # this command was a iteration
    i += 1


# print number from 1 to 5
i = 5
while i >= 1:
    print(i)
    i -= 1

print("Loop ended")

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        break
    else:
        print("finding..")
        i += 1
print("Loop ended")

i = 1
while i <= 10:
    if(i % 2 == 0):
         i += 1
         continue #skip
    print(i)
    i += 1