import sys; sys.path.insert(0,'..')
from solutions.main import *

def test_two_sum_sorted():
    assert two_sum_sorted([2,7,11,15],9) == [1,2]
    assert two_sum_sorted([2,3,4],6) == [1,3]

def test_three_sum():
    result = three_sum([-1,0,1,2,-1,-4])
    assert [-1,-1,2] in result
    assert [-1,0,1] in result

def test_container_water():
    assert container_water([1,8,6,2,5,4,8,3,7]) == 49
    assert container_water([1,1]) == 1

def test_sort_colors():
    assert sort_colors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
    assert sort_colors([2,0,1]) == [0,1,2]

def test_remove_duplicates():
    nums = [1,1,2,3,3]
    k = remove_duplicates(nums)
    assert k == 3

def test_trap_rain():
    assert trap_rain([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_rain([4,2,0,3,2,5]) == 9

def test_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
