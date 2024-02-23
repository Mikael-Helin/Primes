# Set your parameters

X0 = 1          # start value
Xmax = 1400     # max value
N = 1E8         # number of iterations

# Functions

def generator(X):
    return ((2147483647*X + 137438953471) % Xmax + 1)

def step(x):
    x_old = x
    x = generator(x)
    next[x_old-1] = x
    return x

# Finding the primes

primes = [True] * Xmax
primes[0] = False
p=2
while p*p <= Xmax:
    if primes[p-1]:
        for i in range(p*p, Xmax, p):
            primes[i-1] = False
    p += 1

# Initialize variables

X = X0
next = [-1] * Xmax
n = 0

# Find the first prime in the sequence

while not primes[X-1] and n < N:
    X, n = step(X), n+1

# Find a cycle starting from the first prime

prime_sum = X
cycle_start_n = n
cycle_start_prime = X
if n < N:
    X, n = step(X), n+1
    if primes[X-1]:
        prime_sum += X
    while X != cycle_start_prime and n < N:
        X, n = step(X), n+1
        if primes[X-1]:
            prime_sum += X

cycle_length = n - cycle_start_n
cycle_sum = prime_sum - cycle_start_prime
cycles = (N - cycle_start_n) // cycle_length

# Add the remaining primes

n = cycle_start_n + cycles * cycle_length
prime_sum = cycle_start_prime + cycles * cycle_sum
while n < N:
    X, n = step(X), n+1
    if primes[X-1]:
        prime_sum += X

print(f"Prime sum {prime_sum}")
