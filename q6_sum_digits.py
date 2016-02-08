#sum digits

def sum_digits(n):
    n=str(n)
    if len(n)==1:
        return int(n)
    else:
        return int(n[0])+sum_digits(n[1:])

