import numpy as np
from numba import jit, prange, njit
from math import sqrt, floor

# random.seed(1)
rng = np.random.Generator(np.random.MT19937(1)) 

# Parameters
Xmax = 100000000  # Max value for prime generation
N = int(1E8)      # Number of iterations for sequence generation

# Build a np.array of primes
"""
# Too slow

@jit(nopython=True, parallel=True)
def simple_sieve(limit):
    mark = np.ones((limit+1,), dtype=np.bool_)
    primes = np.empty((limit,), dtype=np.int32)
    count = 0
    for p in range(2, limit+1):
        if mark[p]:
            primes[count] = p
            count += 1
            for i in range(p * p, limit+1, p):
                mark[i] = False
    return primes[:count]

@jit(nopython=True, parallel=True)
def mark_segment(primes, start, end):
    segment_size = end - start + 1
    mark = np.ones((segment_size,), dtype=np.bool_)
    for p in primes:
        if p * p > end:
            break
        min_multiple = max(p * p, (start + p - 1) // p * p)
        for i in range(min_multiple, end + 1, p):
            mark[i - start] = False
    return mark

def segmented_sieve(a, b):
    limit = int(np.sqrt(b)) + 1
    primes = simple_sieve(limit)
    
    mark = mark_segment(primes, a, b)
    
    for i in range(a, b + 1):
        if mark[i - a]:
            print(i, end=" ")

numba_primes = simple_sieve(Xmax)[:-1]
primes = np.zeros(Xmax, dtype=bool)
for p in numba_primes:
    primes[p - 1] = True

"""
primes = np.ones(Xmax, dtype=bool)
primes[0] = False
p = 2
while p * p <= Xmax:
    if primes[p - 1]:
        primes[p*p - 1:Xmax:p] = False
    p += 1

# Generate sequence of random numbers
@njit(parallel=True, fastmath=True, nogil=True)
def get_randoms(N, Xmax):
    r = np.empty(N, dtype=np.int32)
    for i in prange(N):
        r[i] = np.random.randint(1, Xmax)
    return r

sequence_np = get_randoms(N, Xmax)
 
# Sum of primes in the generated sequence
@jit(nopython=True, parallel=False)
def sum_primes_numba(sequence, primes):
    sum_primes = 0
    for x in sequence:
        if primes[x - 1]:
            sum_primes += x
    return sum_primes

sum_primes = sum_primes_numba(sequence_np, primes)

print(f"Sum of primes: {sum_primes}")
