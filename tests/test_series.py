import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

def test_fibonacci():
    actual1=fibonacci(0)
    actual2=fibonacci(1)
    actual3=fibonacci(5)
    expected1=0
    expected2=1
    expected3=5
    assert actual1==expected1 
    assert actual2==expected2 
    assert actual3==expected3

def test_lucas():
    actual1=lucas(0)
    actual2=lucas(1)
    actual3=lucas(4)
    expected1=2
    expected2=1
    expected3=7
    assert actual1==expected1 
    assert actual2==expected2 
    assert actual3==expected3

def test_sum_series():
    actual1=sum_series(5)
    actual2=sum_series(1,2,1)
    actual3=sum_series(3,3,4)
    expected1=5
    expected2=1
    expected3=11
    assert actual1==expected1 
    assert actual2==expected2 
    assert actual3==expected3