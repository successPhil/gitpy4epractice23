hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
def computepay(h, r):
    oth = 0
    otr = 1.5 * r
    if h > 40:
        oth = h - 40
        h = 40
    regp = h * r
    otp = oth * otr
    fullp = regp + otp
    return fullp


p = computepay(h, r)
print("Pay", p)