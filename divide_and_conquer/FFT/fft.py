import numpy as np
# A is represented as a coefficient vector of a polynomial
# i.e. a sequence (vector) of numbers computed by a_k * x**k
def fft(A):
    n = len(A)

    # base case 
    if n == 1:
        return A

    # partition even and odd terms
    A_even = [A[x] for x in range(n) if x % 2 == 0]
    A_odd = [A[x] for x in range(n) if x % 2 == 1]  

    # compute A_even(x) = A_even(y) and A_odd(x) = A_odd(y) 
    # (transform to sample vector)
    tA_even = fft(A_even)
    tA_odd = fft(A_odd)

    # nth roots of unity part
    # np.exp(x) computes e^x
    eulers_eq = np.exp(2 * np.pi * (1j / n))

    # combine partitions into polynomial
    root = 1
    A_new = [0] * n
    for x in range(n // 2):
        A_new[x] = A_even[x] + root * A_odd[x]
        A_new[x + (n // 2)] = A_even[x] - root * A_odd[x]
        root *= eulers_eq
    return A_new