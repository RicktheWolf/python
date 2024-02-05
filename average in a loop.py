count = 0
sum = 0
print("Before", count, sum)
for value in [9,47,52.69,1,10]:
    count = count +1
    sum = sum + value
    print(count, sum, value)

print("After", count, sum, sum/count)