# Dynamic Programming
Dynamic programming is an algorithmic technique that uses mathematical optimization. It's specifically useful for any problem that contains *reoccurring subproblems*.

Dynamic programming problems typically fall within these two realms:
* Combinatorics (counting)
* Minimizing or maximizing a value

To put it simply, dynamic programming uses two forms of caching, called **memoization** and **tabulation**, to keep track of subsolutions to small subproblems so that we can use these previous values to solve bigger, overlapping subproblems later on. Eventually, we'll reach a global solution.

Like greedy algorithms, dynamic programming algorithms also use **optimal choices** and **optimal substructures**. However, there's one extra caveat that distinguishes dynamic programming algorithms from greedy algorithms.

## Properties of Dynamic Programming
There are two main properties that suggest that a problem can be solved using dynamic programming:
* Overlapping subproblems
* Optimal substructures

### Overlapping subproblems
Like divide and conquer algorithms, dynamic programming algorithms combine the solutions to subproblems to form a global solution. The thing with dynamic programming is that these solutions to subproblems are often needed *multiple times* throughout the entire algorithm in order to solve bigger subproblems.

As an example, I'll go through how to compute the *n<sup>th</sup>* Fibonacci number to show how subproblems can overlap.

The Fibonacci Sequence is the series of numbers where each term is computed recursively:

```python
fib_sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Intuitively, we can solve the *n<sup>th</sup>* Fibonacci number using naive recursion:

``` python
def naive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return naive_fib(n - 1) + naive_fib(n - 2)
```

If we look at the recursion tree, we can notice some overlapping subproblems. Namely, we recompute the solutions to the subproblems `fib(2)`, `fib(3)`, `fib(4)`, and `fib(5)` multiple times.

![naive-fib-tree](https://i.imgur.com/RCj2bvf.png)

This way of computing takes *exponential* time *O(2<sup>n</sup>)*, since we're needlessly repeating recursive computations that have already been solved.

This is where the defining technique of dynamic programming algorithms - memoization/tabulation - comes in. I'll go over how to implement solution caching in the [variations](#variations) section.

### Optimal substructure
Recall how, for greedy algorithms, we build up to a global solutions by using locally optimal solutions to subproblems. If we write our algorithm in a way where it provides an optimal substructure, our solutions to subproblems are ensured to be optimal.

Dynamic programming works the same way, where we find the optimal solution to a problem of size *n* by splitting into subproblems of size *n' < n*, building up to the globally optimal solution using locally optimal subsolutions to subproblems of size *n'*.

A good example is the infamous [knapsack](https://github.com/bjma/cse-102/tree/master/dynamic_programming/knapsack#optimal-substructure) problem. Check out the link for an indepth explanation of how the optimal substructure of a dynamic programming problem comes into play.

In essence, we form our optimal substructure using memoization.

## Variations
There are two variations to dynamic programming algorithms: **top-down** and **bottom-up**. Both yield the same solutions, but each one builds up to the solution differently.

By convention, it's easier to start with a top-down solution first, then devise a bottom-up solution.

### Top-down 
A top-down algorithm builds a solution in a natural manner, starting from the original problem and working out way down.

Top-down uses **memoization** for storing immediate solutions to subproblems for later use.

Let's go back to our previous example with computing the *n<sup>th</sup>* Fibonacci number, but this time, we'll use memoization to store each immediate solution to our overlapping subproblems.

``` python
# global memoization hashtable {n -> fib(n)} for storing solutions
memo = {}
def fib(n):
    # check if we already solved this subproblem
    if n in memo:
        return memo.get(n)
    if n == 0:
        # add solution to memoization hashtable
        memo.update({n : 0})
        return memo.get(n)
    if n == 1:
        memo.update({n : 1})
        return memo.get(n)
    else:
        f = fib(n - 1) + fib(n - 2)
        memo.update({n : f})
        return f
```

Since we're storing each immediate solution for a subproblem *k < n*, we don't needlessly compute duplicate solutions:

![memo-fib-tree](https://i.imgur.com/wltsYuw.png)

As you can see, this recursion tree only has *n* recursive calls.

### Bottom-up 
Bottom-up algorithms build solutions iteratively, using **tabulation**. We start from the beginning of a problem, and build up our solution to the global solution.

To see this in action, let's rewrite our Fibonacci method into a bottom-up algorithm:

``` python
def bottom_up_fib(n):
    # init tabulation array
    tab = []
    # init known values (base cases)
    tab[0] = 0
    tab[1] = 1
    # iteratively build up to a solution
    for i in range(2, n):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]
```

### Top-down v.s. Bottom-up
Both approaches to dynamic programming have their pros and cons.
| Top-down                              | Bottom-up                                                         |
|---------------------------------------|-------------------------------------------------------------------|
| Slow due to many recursive calls      | Fast since subsolutions are immediately accessed through arrays   |
| Less complex; fewer states            | Complex due to many states/conditions                             |
| Easier to implement                   | Involves harder techniques                                        |
| Only required subproblems are solved  | Every single subproblem is solved                                 |

## Strategy
The general strategy for solving dynamic programming problems uses these following steps:
* Break up problem of size *n* into a series of <ins>overlapping subproblems</ins> of varying sizes *n' < n*.
* Solve each subproblem using an **optimal choice**, defined by a <ins>recurrence</ins>
* Cache immediate solutions to subproblems into a memoization array/hashtable for later use
* Combine solutions to subproblems using an **optimal substructure** in order to build a solution for the overall problem