#sum series 1

def sum_series1(i):
    result = 1/i
    if i==1:
        return 1
    else:
        return (result+sum_series1(i-1))
