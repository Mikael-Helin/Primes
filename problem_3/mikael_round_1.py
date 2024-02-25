import itertools
import numpy as np

# Generate all permutations of the digits 0-9
digits = "0123456789"
permutations = itertools.permutations(digits)

# Convert the permutations to ints
permutations = [int(''.join(p)) for p in permutations]
permutations = np.array(permutations)
copy_permutations = np.copy(permutations)

# Remove all permutations that end with an even number or 5
permutations = [p for p in permutations if p % 10 not in [0, 2, 4, 5, 6, 8]]

# Remove all permutations that are divisible by 3
permutations = [p for p in permutations if p % 3 != 0]

# print the length of the permutations
# No permutations left, so an 9 or 10 digit prime doesn't exist
print(f"Number of permutations left: {len(permutations)}") # Answer: 0

# Copy back the original permutations
permutations = np.copy(copy_permutations)

# Remove the 1 last digits of the permutations
permutations = [p // 10 for p in permutations]

# Remove all permutations that end with an even number or 5
permutations = [p for p in permutations if p % 10 not in [0, 2, 4, 5, 6, 8]]

# Remove all permutations that are divisible by 3
permutations = [p for p in permutations if p % 3 != 0]

# Turn the permutations into a set to remove duplicates
permutations = set(permutations)
permutations = np.array(list(permutations))

# print the length of the permutations
print(f"Number of permutations left: {len(permutations)}") # Answer: 0

# Find the largest number in the permutations
max_num = max(permutations)
print("max_num:", max_num)

# Build a Boolean array of primes up to Xmax = max_num
Xmax = max_num
primes = np.ones(Xmax, dtype=bool)
primes[0] = False
p = 2
while p <= Xmax:
    if primes[p - 1]:
        primes[p*p - 1:Xmax:p] = False
    p += 1

# Now find the largest prime in permutations
max_prime = 0
for num in permutations:
    if primes[num - 1]:
        max_prime = num

print("max_prime:", max_prime) # Answer: 31457269

