# Counting Inversions
Let an *inversion* be defined as the event when two numbers *a* and *b* are in a sequence, where *a > b*.

For example, consider the array:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 4 | 8 |10 | 2 | 6 | 9 |12 |11 | 3 | 7 |

If we **divide** the array into halves like we did with merge sort, we get this subarray for the first half:

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 5 | 4 | 8 |10 | 2 |

I can count *5* inversions:
`5-4`, `5-2`, `4-2`, `8-2`, `10-2`

As for the second half:

|6 | 7 | 8 | 9 |10 |11  |
|---|---|---|---|---|---|
|6  | 9 |12 |11 | 3 | 7 |

We get *8* inversions:
`6-3`, `9-3`, `9-7`, `12-11`, `12-7`, `12-3` `11-3`, `11-7`

Notice that, however, this isn't the total number of inversions in the array.

## Problem
Let `A` be an array with numbers that may or may not be out of order. We must count the number of inversions in the array

### Divide
We previously mentioned that this is similar to merge sort. So, obviously, we divide the array into two subarrays.

However, there's a catch: how do we accurately count the number of inversions in the whole array if we're working with subarrays?

The answer is to divide the array into subarrays, then *sort* each one, comparing the inversions between the two.

### Conquer
After division, all we need to do is count the number of inversions of the two subarrays respectively.

To visualize, here's our two sorted subarrays:

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 2 | 4 | 5 | 8 |10 |

|6 | 7 | 8 | 9  |10 |11 |
|---|---|---|---|---|---|
|3  | 6 |7  |9  |11 |12 |

We count *5* inversions for the first half, and *8* inversions in the second one. 

Recall that we said that we needed to sort both partitions to count all of the inversions. We do this when we **combine** our subarrays.

### Combine
Consider our two subarrays:
| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 2 | 4 | 5 | 8 |10 |

|6 | 7 | 8 | 9  |10 |11 |
|---|---|---|---|---|---|
|3  | 6 |7  |9  |11 |12 |

We can count the number of inversions *between* both sorted subarrays. For example, `A[6] = 3` has *4* inversions when compared to `A[0, ..., 5]`. `A[7] = 6` has *2*, `A[8] = 7` has *2*, then `A[9] = 9` has *1*, giving us a total of *4 + 2 + 2 + 1 = 9* inversions between the sorted subarrays.

Now we merge the arrays:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|11 | 12|

Giving us a total of *5 + 8 + 9 = 22* inversions.

## Algorithm
Notice how, in our design above, our algorithm counts the number of inversions for the each and every subproblem.

Consider this subarray from the previous example:

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 5 | 4 | 8 |10 | 2 |

If we continuously split the subarrays in two:

#### First half

| 0 | 1 | 2 | 
|---|---|---|
| 1 | 5 | 4 |

Split in half again:

| 0 | 1 |
|---|---|
| 1 | 5 |

Getting us two subarrays of size *1*:
| 0 |
|---|
| 1 |


| 1 |
|---|
| 5 |

We can count the inversions as we sort. In this case, there's nothing to be sorted, so we have *0* inversions.

For the other half of this particular subarray,

| 2 | 
|---|
| 4 |    

If we compare it with the sorted subarray:

| 0 | 1 |
|---|---|
| 1 | 5 |

We can count *1* inversion.

#### Second half

| 3 | 4 | 5 |
|---|---|---|
| 8 |10 | 2 |

This is kind of the same case as the previous example. There are *2* inversions if we follow the same steps.

*1 + 2* inversions gives us *3* total inversions for the number of inversions in both halves.

#### Combining
Now compare the first (left) sorted subarray to the second (right) sorted subarray:

| 0 | 1 | 2 | 
|---|---|---|
| 1 | 4 | 5 |

| 3 | 4 | 5 |
|---|---|---|
| 2 | 8 |10 |

We count a total of *2* inversions between the two, namely `A[3] = 2`. Thus, *3 + 2 = 5* total inversions for this half of the subarray.

So, we need a method that both counts inversions and sorts the subarray. Let's call this `sort_and_count()`.

``` python
def sort_and_count(A):
    if len(A) == 1:
        return 0
    else:
        # partition array
        left_bound = len(A) / 2
        right_bound = len(A) - left_bound
        L = [A[x] for x in range(left_bound)]
        R = [A[x] for x in range(right_bound)]

        # now sort and count both
        L_inv, L = sort_and_count(L)
        R_inv, R = sort_and_count(R)
        # then merge both subarrays
        inv = merge_and_count(L, R)
        # return number of inversions and new sorted array
        return num_inversions = L_inv + R_inv + inv, A
```

All we have to do is implement the merge method. This method uses some tricks using the fact that all elements are sorted. 

Since both `L` and `R` are sorted, we know that if for some `j` and `i` where `R[j] < L[i]`, then `R[j] < L[i, ..., n]`. Else, then this implies that `R[j] >= L[i]`, meaning `R[j, ..., m] >= L[i]`, thus no inversions.

``` python
def merge_and_count(L, R):
    n = len(L) - 1
    m = len(R) - 1
    # temp array for merging
    A = []
    i = j = 0
    count = 0
    while L and R:
        # append min value; we do this
        A.append(min(min(L), min(R)))
        # if there is an inversion at j,
        # then count for the rest starting at i
        if R[j] < L[i]:
            # we can also use n - (i + 1)
            count += [1 for x in range(i + 1, n)]
            # now look at next element in R
            # to find more inversions
            j += 1
        else:
            # else, no need to look so continue
            i += 1
    # if L is empty, append the rest of R into list
    # this is fine since it's sorted
    if not L:
        for x in range(j, m):
            A.append(R[x])
    # likewise if R is empty
    if not R:
         for x in range(i, n):
            A.append(L[x])
    # return count and sorted merged array
    return count, A
```