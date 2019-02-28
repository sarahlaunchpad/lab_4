# Sarah Murphy
#mypower.py

def power(base, exponent): #formal parameters
    result = 1
    for counter in range (exponent):
        result = result * base
    return result

answer = power(-1,3)
print( answer)
# return result, now having value n**r
