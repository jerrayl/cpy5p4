#find gcd

def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
    
def test():
    if gcd(24,16)==8 and gcd(255,25)==5:
        return True
    else:
        return False
