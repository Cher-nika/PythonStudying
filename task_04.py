"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from random import *


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    la = len(a)
    assert la >= 0 and la <= 1000
    assert la == len(b) and la == len(c) and la == len(d)
    i, j, k, l = 0, 0, 0, 0
    res = int(0)
    while i < la:  # iterating over the values to count
        while j < la:
            while k < la:
                while l < la:
                    if a[i] + b[j] + c[k] + d[l] == 0:
                        res += 1
                    l += 1
                k += 1
            j += 1
        i += 1
    return res
