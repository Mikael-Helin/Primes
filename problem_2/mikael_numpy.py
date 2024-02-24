import numpy as np
import random

# random.seed(1)
rng = np.random.Generator(np.random.MT19937(1)) 

# Parameters
Xmax = 100000000  # Max value for prime generation
N = int(1E8)      # Number of iterations for sequence generation

# Build a np.array of primes
primes = np.ones(Xmax, dtype=bool)
primes[0] = False
p = 2
while p * p <= Xmax:
    if primes[p - 1]:
        primes[p*p - 1:Xmax:p] = False
    p += 1

# Generate sequence of random numbers using random.randint
#sequence = [random.randint(1, Xmax) for _ in range(N)]
#sequence_np = np.array(sequence)  # Convert to NumPy array for efficient processing

# np.random.randint does not generate the same sequence as random.randint
sequence_np = rng.integers(1, Xmax, N)

# Sum of primes in the generated sequence
# Here, we directly use the primes array for checking primality
sum_primes = np.sum(sequence_np[primes[sequence_np - 1]])

print(f"Sum of primes: {sum_primes}")
