def dec_2_fact_string(nb):
    factorial_string, i = '', 1
    while nb != 0:
        factorial_string += str(nb % i)
        nb = nb // i
        i += 1
    return factorial_string[::-1]
    
def fact_string_2_dec(string):
    pass

print(dec_2_fact_string(463))



    
