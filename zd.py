from math import *

def dec_2_fact_string(nb):
    factorial_string, i = '', 1
    while nb != 0:
        factorial_string += str(nb % i)
        nb = nb // i
        i += 1
    return factorial_string[::-1]
    
def fact_string_2_dec(string):
    string, nb = [int(string[i]) for i in range(len(string))], 0
    for i in range(len(string)):
        print(nb * (len(string) - i) + (string[i]))
        nb = nb * (len(string) - i) + (string[i])
    return nb

print(dec_2_fact_string(463))
print(fact_string_2_dec("341010"))



    
