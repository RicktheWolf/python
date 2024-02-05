largestNumber = -1
print("Before",largestNumber)
for num in [9,41,45,12,13,19,69]:
    if num > largestNumber:
        largestNumber = num
    print(largestNumber,num)

print("After",largestNumber)