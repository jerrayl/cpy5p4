#find uppercase

def find_num_uppercase(string):
    if str[len(string) - 1].isupper():
        if len(string) == 1:
            return 1
        else:
            return 1 + find_num_uppercase(string[:-1])
    else:
        if len(string) == 1:
            return 1
        else:
            return find_num_uppercase(string[:-1])


