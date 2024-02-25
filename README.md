# Primes

In this taks, we want to benchmark OpenAI's ChatGPT 4 vs Google's Gemini Advanced 1.5.

## The problem

To solve this problem, you are not allowed to use any external libraries. Also, you have to make this algorithm as fast as possible. The code has to be written in Python.

There is a sequence of numbers generated by the formula

    X(0) = 1
    X(n+1) = mod(2147483647*X(n)+137438953471, 1400) + 1

Your task is to take all prime numbers from the sequence X(1), ..., X(1E8) and sum them together. Note, we do not include X(0) in the series.

## Results - Round #1

This is the first round of test. Where, I, chatGPT and Gemini did not use the knowledge from each others.

### gemini_round_1.py

Gemini built an boolean array of prime numbers.

Correct answer: 19268573182

Timings of 3 runs

    real    0m24.866s
    user    0m24.784s
    sys     0m0.077s

    real    0m26.550s
    user    0m26.475s
    sys     0m0.068s

    real    0m26.132s
    user    0m26.035s
    sys     0m0.092s

### chatgpt_round_1.py

ChatGPT built a set of prime keys.

ChatGPT says

    "A key insight to optimize further is recognizing patterns or cycles within the sequence generated by the formula. Due to the modulo operation, the sequence might enter a cycle where the same numbers start repeating after a certain point. This would drastically reduce the number of unique values we need to check for primality.

    Let's refine our strategy with a focus on identifying a cycle within the sequence. If a cycle is detected, we can calculate the sum of primes within one cycle and then use this information to compute the total sum for all cycles up to X(100,000,000)X(100,000,000) without iterating through every single value.

    1) Detect a cycle: Modify the sequence generation to detect a cycle.
    2) Compute sum within the cycle: Once a cycle is detected, compute the sum of primes within that cycle.
    3) Extrapolate to the total sum: Calculate how many complete cycles fit into 100,000,000 iterations and sum accordingly."

However, CharGPT did not use it's own idea.

Correct answer: 19268573182

Timing from 3 runs

    real    0m17.221s
    user    0m17.215s
    sys     0m0.004s

    real    0m17.185s
    user    0m17.175s
    sys     0m0.008s

    real    0m18.033s
    user    0m18.030s
    sys     0m0.000s

### mikael_round_1.py

I built a dictionary of prime keys.

Correct answer: 19268573182

Timing from 3 runs

    real    0m28.495s
    user    0m28.489s
    sys     0m0.004s

    real    0m29.795s
    user    0m29.784s
    sys     0m0.008s

    real    0m29.267s
    user    0m29.256s
    sys     0m0.005s

## Results - Round #2

We have been allowed to see each others code and from there make improvements.

### gemini_round_2.py

This time Gemini came up with the wrong answer and it was also slower.

Wrong answer: 69799288914

    real    0m49.675s
    user    0m47.964s
    sys     0m1.704s

I then attempted to make Gemini use repeated cycles, as ChatGPT suggested, and it came up again with a bad solution.

Wrong answer: 69799288864

    real    0m31.977s
    user    0m30.185s
    sys     0m1.785s

### chatgpt_round_2.py

This time ChatGPT used its own idea of cycles and the improvement was drastic!

Correct answer: 19268573182

    real    0m0.018s
    user    0m0.014s
    sys     0m0.004s

    real    0m0.013s
    user    0m0.013s
    sys     0m0.000s

    real    0m0.019s
    user    0m0.011s
    sys     0m0.008s


### mikael_round_2.py

I combines ideas from Gemini and ChatGPT.

Correct answer: 19268573182

    real    0m0.016s
    user    0m0.012s
    sys     0m0.004s

    real    0m0.013s
    user    0m0.007s
    sys     0m0.007s

    real    0m0.017s
    user    0m0.007s
    sys     0m0.011s


## Follow up problem

There is a sequence of cyclic numbers generated by the code

    import random
    random.seed(1)

    def generator():
        return random.randint(1, 100000000)

Your task is to take all prime numbers from the sequence X(1), ..., X(1E8) and sum them together. The first generated number of generator() is X(1). You have to makes this solver as fast as possible.

### chatgpt.py

ChatGPT had to try around a bit and know my system before it solved this problem.

This is the output.. not bad, a bit over a minute

    279337398623953 5761455

    real    1m18.887s
    user    1m18.654s
    sys     0m0.225s

ChatGPT:

    That's an impressive result! Completing the task in a bit over a minute and successfully summing the prime numbers generated within the specified range to a total of \(279,337,398,623,953\) demonstrates both the effectiveness of the Sieve of Eratosthenes for prime generation and the capability of your system to handle such intensive computations efficiently. Additionally, the output confirms that there are \(5,761,455\) prime numbers up to \(100,000,000\), which aligns with known prime counts within that range.

    This performance is quite good, considering the scale of the task. It showcases the power of using efficient algorithms for prime generation and the advantage of having a robust computing environment.

    If you have any more questions or need further assistance with similar tasks or optimizations, feel free to ask!

### mikael.py

My approach is to build a list of primes... and it is slower than the ChatGPT solution.

    279337398623953

    real    1m25.252s
    user    1m25.166s
    sys     0m0.076s

Using dictioanry of primes took 2 minutes and 40 seconds.

First when I passed in the prime numbers as a function it got a little faster...

    real    1m20.556s
    user    1m20.442s
    sys     0m0.092s

### mikael_numpy.py

Giving together ChatGPT and Gemini a final shot with Numpy.

    Sum of primes: 279337398623953

    real    0m55.339s
    user    0m54.281s
    sys     0m1.724s

If we were to use number generation with numpy, it gets fast... unfortunately np.random.randint does not use the same generator as random.randint.

    Sum of primes: 279137654125969

    real    0m3.114s
    user    0m3.096s
    sys     0m0.529s

## Yet another problem

Find the largest prime where all digits are different. Naturally, this prime is smaller than the number 9876543210. Using permutations is allowed, if you think it speeds up computation.

Gemini

    The largest prime with unique digits is: 1234657

ChatGPT

    101

Mikael

    98765431