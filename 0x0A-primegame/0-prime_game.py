#!/usr/bin/python3
""" Prime Game """
def sieve_of_eratosthenes(max_num):
    """ Sieve of Eratosthenes"""
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def prime_game(n, primes):
    """ Prime Game"""
    remaining = list(range(n + 1))
    move = 0  # 0 for Maria, 1 for Ben
    while True:
        made_move = False
        for i in range(2, n + 1):
            if primes[i] and remaining[i] != -1:
                made_move = True
                for j in range(i, n + 1, i):
                    remaining[j] = -1
                move = 1 - move
                break
        if not made_move:
            break
    return "Ben" if move == 0 else "Maria"


def isWinner(x, nums):
    """ Prime Game"""
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = prime_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
