def computepay(h, r):
    if h > 40:
        reg = h * r
        otp = (h - 40) * (r * 0.5)
        pay = reg + otp
    else:
        pay = h * r
    return pay


h = float(input("Enter hours worked:"))
r = float(input("Enter Pay rate:"))
Gross_Pay = computepay(h, r)
print("Gross Pay", Gross_Pay)
