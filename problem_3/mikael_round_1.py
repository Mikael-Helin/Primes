import itertools
import numpy as np

# Generate all permutations of the digits 0-9
digits = "01234567890"
permutations = itertools.permutations(digits)

# Convert the permutations to strings
permutations = [int(''.join(p)) for p in permutations]

# Remove all permutations that start with 0
permutations = [p for p in permutations if str(p)[0] != '0']

# Remove all permutations that end with an even number or 5
permutations = [p for p in permutations if str(p)[-1] not in ['0', '2', '4', '5', '6', '8']]

# Convert the permutations to np integers
permutations = np.array(permutations)

# Find the largest number in the permutations
max_num = max(permutations)

# Build a Boolean array of primes up to Xmax = 1E9
Xmax = 1000000000
primes = [True] * Xmax
primes[0] = False
p=2
while p*p <= Xmax:
    if primes[p-1]:
        for i in range(p*p - 1, Xmax, p):
            primes[i] = False
    p += 1

# Rwmove all permutations that are divisible by numbers in the primes array
permutations = [p for p in permutations if not any(p % i == 0 for i in range(2, int(p**0.5) + 1))]

# print the length of the permutations
print(len(permutations)) # answer: 0