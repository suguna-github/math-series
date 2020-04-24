from math_series import fibonacci
from math_series import lucas
from math_series import sum_series

# test for test
def test_fibonacci():   
    assert fibonacci(0) == 0

def test_fibonacci1():    
    assert fibonacci(1) == 1

def test_fibonacci2():
    assert fibonacci(2) == 1

def test_fibonacci3():
    assert fibonacci(3) == 2

def test_lucas_test1():
    assert lucas(0) == 2

def test_lucas_test2():
    assert lucas(1) == 1

def test_lucas_test3():
    assert lucas(2) == 3

def test_sum_series_fibonacci0():
    assert sum_series(2) == 1

def test_sum_series_fibonacci1():
    assert sum_series(4) == 3

def test_sum_series_lucas_1():
    assert sum_series(1,2,1) == 1

def test_sum_series_lucas_2():
    assert sum_series(2,2,1) == 3

def test_sum_series_lucas_3():
    assert sum_series(3,2,1) == 4

def test_sum_series_lucas_4():
    assert sum_series(4,2,1) == 7    

def test_sum_series_lucas_5():
    assert sum_series(5,2,1) == 11
