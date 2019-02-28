# Sarah Murphy
# test_mypower.py
#import mypower is a good option when testing another file.

def power(base, exponent):
    result = 1
    for counter in range (exponent):
        result = result * base #result*= base
    return result

answer = power(5,2)
print("base '**' exponent is ", answer)

def test_one_to_1():
    assert power(1,1) == 1

def test_6_to_0 ():
    assert 1 == power (6,0)

def test_minus_2_to_1():
    assert -2 == power(-2, 1)

def test_0_to_5():
    assert 0 ==power(0,5)

def test_2_to_5():
    assert 32 == power(2,5)

def test_minus1_to_3():
    assert -1 == power(-1,3)

def test_ten_to_10():
    assert 10000000000 == power(10,10)

def test_four_to_5():
    assert 1024 == power(4,5)

def test_7_to_2():
    assert 49 == power(7,2)

def test_6_to_2():
    assert power (6,2) == 36

def test_1_to_49():
    assert 1 == power(1,49)