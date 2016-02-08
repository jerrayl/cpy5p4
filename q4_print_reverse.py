# print reverse

def reverse_int(n):
    n = str(n)
    if len(n) == 1:
        return n[0]
    else:
        return n[len(n) - 1] + reverse_int(n[:-1])

