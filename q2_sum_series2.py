#sum series 2

def sum_series2(i):
    result=i/(2*i+1)
    if i==1:
        return 1
    else:
        return result+sum_series2(i-1)

