# Merge Sort
Merge sort is pretty much everyone's introduction to divide and conquer algorithms.

The general idea is: how can we make an efficient sorting algorithm that runs faster than *O(n<sup>2</sup>)* time?

Consider the array:
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
|38 |27 |43 |3  |9  |82 |10 |

How do we sort this array using divide and conquer strategies?

## Subproblems
The reason why merge sort is a fan favorite introduction to divide and conquer is because how easy it is to find what subproblems we're going to deal with.

Let's consider the base cases and exit clause. We know that we can't sort an array if it only contains one value:
| 0 |
|---|
|38 |

So, this is our exit clause.

What about if our array has two elements?

| 0 | 1 |
|---|---|
|38 |27 |

We can only do one thing; if the elements are out of order, swap them. If not, leave them as is:

| 0 | 1 |
|---|---| 
|27 |38 |

## Divide
Now that we know our exit clause and base case, all we have to do is divide. If we continuously divide the array into half-length subarrays, we can reach both our exit clause (array w/ one element) or base case (array w/ two elements). 

Observe what happens when we divide our array into two halfs, then continue to do this for each array:

#### First half

| 0 | 1 | 2 | 3 |
|---|---|---|---|
|38 |27 |43 |3  |

Divide into half again:

| 0 | 1 |
|---|---|
|38 |27 |

We reach a subproblem of an array with two elements. They're not sorted, so we can swap them.

| 0 | 1 |
|---|---| 
|27 |38 |

This is the identical case for the other half:

| 2 | 3 |
|---|---|
|3 |43  |

Then, we merge them using some `merge()` method.

#### Second half

| 4 | 5 | 6 |
|---|---|---|
|9  |82 |10 |

Divide the subarray into halves:

| 4 | 5 |
|---|---|
|9  |82 |

These are already in order, so we don't do anything.

Other half:
| 6 |
|---|
|10 |

This is one of our base cases, which we do nothing. Now we just merge the two subarrays.

This is what our final solution looks like as a recursion tree:

![merge-sort](https://www.gyanblog.com/assets/img/2019/merge_sort.png)

## Algorithm
Let's write the algorithm for merge sort. 

Let `A` be an array of integers, where `l` is our lower bound for each subarray, and `u` be the upper bound. `m` is the middle index of each subarray.

First, let's define the function `merge()`:
``` python
def merge(A, l, m, u):
    # initialize two subarrays and copy data
    L = [A[x] for x in range(m - l + 1)]
    R = [A[x] for x in range(u - m)]

    # index for L and R
    i = j = 0

    # index for merged subarray
    k = 1
    # merge by sorting then copying L and R elements into A
    while (i < len(L) and j < len(R)):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    # copy remaining elements of L and R into A
    while (i < len(L)):
        A[k] = L[i]
        i += 1
        k += 1

    while (j < len(R)):
        A[k] = R[j]
        j += 1
        k += 1
```
Notice how we actually do the sorting when we merge. This actually doesn't sort out the *entire* array, but just the ones that we've looked at when merging, hence the last part where we store all uncopied elements into the array in an unordered fashion.

Our `sort()` method should actually just partition our subarrays so we can sort them in `merge()`.

``` python
def sort(A, l, u):
    # still within bounds
     if (l < u):
        # get middle index
        m = (l + u) / 2

        # divide array into halves
        sort(A, l, m)
        sort(A, m + 1, u)

        # merge them
        merge(A, l, m, u)
```

And there, we have our merge sort algorithm. If we wanted to call it, we'd use `sort(A, 0, len(A) - 1)`.

    
