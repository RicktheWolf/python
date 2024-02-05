num1= 20
num2= 10

#instead of doing
"""if num1>num2:
    print(num1)
else:
    print(num2)"""
#we can use ternary opeartors like this

max= (num1 if num1>num2 else num2)

print("Maximum number is = ",max)