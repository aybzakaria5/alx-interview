#!/usr/bin/python3
"""min operations"""


def minOperations(n):
    """min operations"""
    if n <= 1:
        return 0
    operations = [0] * (n + 1)
    for i in range(2, n + 1):
        if n % i == 0:
            operations[i] = i
            for j in range(i // 2, 1, -1):
                if i % j == 0:
                    operations[i] = min(operations[i], operations[j] + (i // j))
    return operations[n]
