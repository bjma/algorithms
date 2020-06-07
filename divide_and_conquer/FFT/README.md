# Fast Fourier Transform
This algorithm is a bit of a complicated concept. It's extremely math-heavy, particularly in linear algebra.

Essentially, Fast Fourier Transform (FFT) is an algorithm used to convert between different forms of polynomials, specifically from coefficient vector representation to sample vector representation, vice versa.

To visualize, let's first define some ways to represent polynomials. Click [here](#algorithm) if you want to skip all the conceptual stuff, but I recommend reading through it!

## Polynomial representations
Displayed below is a polynomial *A(x)* consisting of the sum of the product between coefficient *a* and variables *x* until some degree *n*.

![poly-sum](https://i.imgur.com/p6q2Fxl.png)

The above equation can also be called the **coefficient vector** (vector of *a<sub>k</sub>x<sup>k</sup>* values).

A **sample vector** is represented as the pair (*x<sub>k</sub>*, *y<sub>k</sub>*), which allows us to compute some polynomial *A(x)* at *x<sub>k</sub>* by simply accessing the *y* value, i.e. *A(x<sub>k</sub>) = y<sub>k</sub>* .

To visualize, recall how, back in linear algebra, we found it easier to work with polynomials if we represent the polynomial equation as a matrix, consisting of three components:

![poly-mat](https://i.imgur.com/upWfbNA.png)

Breaking this down, we essentially have *m* polynomial equations with degree *n* that can be formed by the matrix product between the coefficient vector *A* and the Vandermonde matrix *V*, which gives us some output in the vector *Y*. 

## Conversion
Let's think back to solving matrix systems. How can we convert *A* to *Y*? If you paid attention to what I wrote above, and looked at the picture, then you know what I'm about to say: we simply get the matrix product between *V* and *A* to get a vector *Y*.

![mat-prod](https://i.imgur.com/TRe9FTc.png)

Vice versa, if we wanted to convert *Y* to *A*, we would need to use Gaussian elimination (or dot product of *V<sup>-1</sup>* and *Y*) to solve for *A* (I used the symbol for matrix solving in `MATLAB`):

![gauss-elim](https://i.imgur.com/5xfA0Pm.png)

### Why conversion?
You might be wondering why we even want to convert between coefficient and sample vectors in the first place. Well, if you're a software engineer, chances are that you don't ever have to. However, it is useful to know FFT because of its relation to *runtime*.

Consider the conversions we defined above. 

What's the runtime of a program that computes the product between two polynomials *A(x)* and *B(x)* of degree *n*? 

Let such a polynomial product be written as *C(x) = A(x)B(x)*.

If we represented the polynomials as **coefficient vectors**, i.e. *A(x) = a<sub>0</sub> + a<sub>1</sub> x + a<sub>2</sub>x<sup>2</sup> + ... + a<sub>n - 1</sub>x<sup>n - 1</sup>* and *B(x) = b<sub>0</sub> + b<sub>1</sub> x + b<sub>2</sub>x<sup>2</sup> + ... + b<sub>n - 1</sub>x<sup>n - 1</sup>*, we'd have to multiply each and every term of both polynomials, which gives us a runtime of *O(n<sup>2</sup>)*.

What about the runtime if we represented *A(x)* and *B(x)* as **sample vectors**, where *A(x<sub>k</sub>) = y<sub>k</sub>* and *B(x<sub>k</sub>) = y<sub>k</sub>*? All we need to do is multiply *A(x<sub>A</sub>)B(x<sub>B</sub>) = y<sub>A</sub>y<sub>B</sub>* for each term in each polynomial, which takes us *O(n)* time.

What about the runtime when we want to do **polynomial evaluation**, i.e. given a polynomial *A(x)* and a number *x<sub>k</sub>*, determine *A(x<sub>0</sub>)*?

If we used sample vectors, this would be pretty difficult. I won't delve deeper into how, but in short we would need to do [polynomial interpolation](https://en.wikipedia.org/wiki/Polynomial_interpolation#:~:text=In%20numerical%20analysis%2C%20polynomial%20interpolation,the%20points%20of%20the%20dataset.), which takes quadratic time, or *O(n<sup>2</sup>)*.

However, if we represented *A(x)* as a coefficient vector, all we have to do is plug in *x<sub>k</sub>* for all *x* terms in *A(x)*, which just takes *O(n)* time!

### Conclusion for reason behind conversion
As you can see, polynomial operations have different computational complexities for different representations. To perform polynomial operations as efficiently as we can, we need to convert between different representations. The problem is, how can we convert between representations efficiently? 

Take a look at the two conversions I wrote above. What are the runtimes for each?
* Coefficient vector → sample vector: *O(n<sup>3</sup>)*
* Sample vector → coefficient vector: *O(n<sup>3</sup>)* for the inverse method and Gaussian elimination

The goal is to come up with an efficient algorithm that does this conversion for us.

*This* is what **Fast Fourier Transform** is: an algorithm that converts between a coefficient vector and a sample vector of a polynomial, running in *O(nlogn)* time

## Algorithm
Now we need to devise a divide and conquer algorithm for performing conversions between polynomial representation. This part is also pretty math-heavy.

**Goal**: Compute *A(x)* by converting it from coefficient vector into a sample vector, ∀*x ∈ X*, where *X* is our Vandermonde matrix.

### Divide
In the previous divide and conquer algorithms we went through, we simply divided our problem into equal length partitions. However, for FFT, we're going to do something different.

This is because simply dividing our polynomia *A(X)* into equal length partitions won't do much in the scope of converting to a different form. Instead, we divide them into two partitions, one containing all **even** terms and another containing all **odd** terms. This way, we split the polynomials into half of the degree *n*.

![divide-poly](https://i.imgur.com/S2rf258.png)

### Conquer
Now, to compute *A(X)*, we need to recursively compute all the outputs for both the even and odd partitions of the polynomial.

So, our conquering involves computing `A_even(x) = A_even(y)` and `A_odd(y) = A_odd(y)` for every output `y` that maps to some `x**2` (x<sup>2</sup>) in the set of all squared x, *X<sup>2</sup> = {x<sup>2</sup> | x ∈ X}*:

![conquer-poly](https://i.imgur.com/oykhFsr.png)

#### Why only X<sup>2</sup>?
Intuitively, the more data or inputs we have, the worse an algorithm's computational complexity is, if we write it in a naive way.

However, if we *square* a set of inputs/data, we can actually *reduce* the cardinality of the set. Observe:

![reduce-cardinality](https://i.imgur.com/Ku5MWZH.png)

We can see that squaring a set reduces its cardinality. 

This is because of the **n<sup>th</sup> root of unity**, which is some complex number *x* s.t. *x<sup>n</sup> - 1 → x<sup>n</sup> = 1*, where the degree *n* of the polynomial is positive.

There's a theorem which states,
> If *n* is even, then there will be 2 real solutions to *x<sup>n</sup> = 1*, e.g. *-1* and *1* for *x + 1*.

We can actually see this happening in the example above. If *|X| = 2*, then we have a set *X = {-1, 1}*. This is the solution to the *2<sup>nd</sup>* root of unity, where *X<sup>2</sup> = {1} = x + 1* (polynomial of degree *n = 2*). Try replicating this example for when *|X| = 4* (polynomial of degree *n = 4*, or *x<sup>2</sup> + 1*) to understand what I'm showing.

*TL;DR* - Squaring a set of numbers at the *n<sup>th</sup>* root of unity reduces its cardinality. 

### Combine
Now, all we have to do is combine our two polynomials into the original polynomial.
![combine-poly](https://i.imgur.com/NvxigVD.png)

## Solution
Below is the Python code for Fast Fourier Transform:

``` python
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
```

## Extra: Inverse FFT
If we wanted to convert a polynomial from its sample vector representation to a coefficient vector, we use the *inverse* Fast Fourier Transform.














