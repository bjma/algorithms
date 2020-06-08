# Median of Two Databases (#1)
Taken from: "Divide and Conquer." *Algorithm Design*, John Kleinberg, et. al.

## Problem
You are interested in analyzing some hard-to-obtain data from two separate databases. Each database contains *n* numerical values so that there are *2n* values total. You may assume that no two values in both databases are the same. 

We want to determine the median of this set of *2n* values, which we will define here to be the *n<sup>th</sup>* smallest value.

The only way we can access these values is through *queries* to the databases. In a single query, you can specify a value *k* to one of the two databases, and the chosen database will return the *k<sup>th</sup>* smallest value that it contains. Since queries are expensive, we want to compute the median using as few queries as possible.

Give an algorithm that finds the median value using at most *O(nlogn)* queries.

### Median 
The median is the middle number in a sorted (ascending or descending) serires of numbers.

**E.g.** Given the data set {3, 13, 2, 34, 11, 26, 47}, determine the median.

If we sort it, we get {2, 3, 11, <ins>13</ins>, 26, 34, 47}, where the median is underlined. This is a pretty clear cut case where the size our data set is odd.

Let's add *17* into our data set so that we have an even-sized data set: {2, 3, 11, 13, 17, 26, 34, 47}. To get the median, we get the average between the two middle elements *(13 + 17) / 2* = *15*.

## Solution
Let `A` and `B` be a list representing each database, where `A[i]` and `B[i]` are the *i<sup>th</sup>* smallest elements of `A` and `B`.

In order to find the median of `A` and `B`, we first need to sort both of these lists. This way, for all `k` in `A` and `B`, `A[k - 1] < A[k]` and `B[k - 1] < B[k]`. This way, the median value should be at index `i = n // 2`.

The idea behind the divide and conquer approach to this problem is to first compute the respective median of `A` and `B`, then dividing our search space based on the median values.

First, let's compare the respective median of `A` and `B`, which we'll call `A[k]` and `B[k]`, where `k = n // 2`. If `A[k] < B[k]`, then this implies that `B[k] > A[1:k]`. Also note that `B[k] > B[1:k - 1]` by definition of the median (and because we sorted the array). Because `B[k]` is greater than  `k` values in both `A` and `B`, we can say `B[k]` is the least *2k<sup>th</sup>* element in the combined data bases. 

However, this doesn't mean that `B[k]` is the median of both databases. We want the *n<sup>th</sup>* smallest number in both databases, not the *2k<sup>th</sup>*.

To visualize this, let's use these two databases as an example:

``` python
# first data base
A = [1, 12, 15, 26, 28]
# second data base
B = [2, 13, 17, 30, 45]
# num values
n = len(A)
```

Compare the two medians:
``` python
# get middle index
k = n // 2
# medians
A[k] = 15
B[k] = 17
# since 17 > 15, let's look at B[k]
```

We can see how `B[k]` is the least *2k<sup>th</sup>* value, but not the median:

``` python
# unsorted combined database
C = [1, 12, 15, 26, 28, 2, 13, 17, 30, 45]
# sorted combined database
C = [1, 2, 12, 13, 15, 17, 26, 28, 30, 45]
```

Since *2k >= n*, all elements that are greater than `B[k]` are greater than the median are irrelevant information since they don't help us find the median of both databases. Additionally, since all elements in `A[1:k - 1] < B[k]`, the first `k - 1` elements in `A` are also irrelevant data. Therefore, it makes sense to remove the last `n - k` elements in `B`, and remove the first `k` elements in `A`, keeping the median each time:

``` python
# first data base
A = [15, 26, 28]
# second data base
B = [2, 13, 17]
# reduced search space in sorted combined database
C = [2, 13, 15, 17, 26]
```

We can see that we're reducing our search space so that we approach the middle portion of the combined database. This is because `B[k] > A[k]` implying that the global median is to the right of `A[k]` and to the left of `B[k]`. 

If we continue to divide our databases, we can see a base case that forms:

``` python
# first data base
A = [15, 26, 28]
# second data base
B = [2, 13, 17]
# medians
A[k] = 26
B[k] = 13
# 26 > 13, so divide w/ respect to A
A = [15, 26]
B = [13, 17]
```

Can you get a sense of what our base case is? If we look at our sorted combined database again:

``` python
C = [1, 2, 12, 13, 15, 17, 26, 28, 30, 45]
```

We get the median `(15 + 17) // 2 = 16`, which is clearly the max of `A[0]` and `B[0]` and the min of `A[1]` and `B[1]`:

``` python
A = [(15), 26]
B = [13, (17)]
```

This is because we know that any values less than a median are irrelevant to finding a global median, same thing with the values that are greater than.

So, with the way we're dividing, we always reach this base case:

``` python
if (n == 2):
    return (max(A[0], B[0]) + min(A[1], B[1])) // 2
```

## Algorithm
``` python
def get_median(A, B, n):
    # no solution
    if n == 0:
        return -1
    elif n == 1:
        return (A[0] + B[1]) // 2
    elif n == 2:
        return (max(A[0], B[0]) + min(A[1], B[1])) // 2
    else:
        k = n // 2
        m1 = A[k] if n % 2 == 1 else (A[k] + A[k - 1]) // 2
        m2 = B[k] if n % 2 == 1 else (B[k] + B[k - 1]) // 2

        if m1 < m2:
            return get_median(A[k:], B[:k + 1], k)
        else:
            return get_median(A[:k + 1], B[k:], k)
```









