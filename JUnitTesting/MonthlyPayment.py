def payment(principal, year, rate):
    n = 12 * year
    r = rate/(12*100)
    amount = (principal * rate)/(1 - (1 + r)**(-n))
    return amount


print(payment(2000, 2, 2))

