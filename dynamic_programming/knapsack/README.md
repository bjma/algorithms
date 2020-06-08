# Knapsack Problem
The [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) is a pretty famous interview problem that uses dynamic programming. 

There are two variations, the simple Knapsack problem (where you can use a greedy heuristic to solve the problem), and the 0-1 Knapsack problem, which forces you to either *choose* or *not choose* to collect an item (binary choice).

## Problem
Imagine that you are a robber breaking into a house to steal some `n` items. You are carrying a knapsack with a maximum weight capacity `C`, and can choose any number of items with an associated weight `w` and value `v`, so long as the total weight of the items you chose don't exceed the capacity `C`.

Below is a simple visualization of the problem.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Knapsack.svg/500px-Knapsack.svg.png)

### Breaking it down
Consider the following set of items, represented as tuples containing a value `v` and a weight `w`. 
``` python
items[0] = None
# item 1: v1 = 2, w1 = 3
items[1] = (2, 3)
# item 2: v1 = 2, w1 = 1
items[2] = (2, 1)
# item 3: v1 = 4, w1 = 3
items[3] = (4, 3)
# item 4: v1 = 5, w1 = 4
items[4] = (5, 4)
# item 5: v1 = 3, w1 = 2
items[5] = (3, 2)
```

Let our maximum capacity of the knapsack be `C = 7`.

What subset of the item set maximizes value while minimizing weight? (Note that we can go up to max. capacity so long as we have the maximum possible weight)

If you thought `items[2] + items[4] + items[5]`, you're right! Let's see what happened here:
``` python
items[2] + items[4] + items[5] = (2, 1) + (5, 4) + (3, 2)
```
We get a total value of `2 + 5 + 3 = 10` with a total weight of `1 + 4 + 2 = 7`.

### Intuition and overlapping subproblems
How did we reach this conclusion? 

First, consider the capacity `C = 7`. If we choose `items[1]`, then our current value would be `current_val = 0 + 2 = 2`, and our capacity would be cut down to `C = 7 - 3 = 4`. We then have a new capacity, and must select items accordingly as to not exceed this new capacity.

Below is a somewhat simple visualization of how our capacity changes as we choose items:
``` python
# current capacity 
C = 7
# total value accumulated
total_val = 0
# set of items we can choose from
items = [(0, 0), (2, 3), (2, 1), (4, 3), (5, 4), (3, 2)]
```
Here's how our solution unfolds if we chose `items[1]` as the first one to put into our knapsack:
``` python
# C = 7 - 3
C = 4
# total_val = 0 + 2 
total_val = 2

# now that we have a new capacity C = 4, then we only 
# have a few items to choose from: items 2, 3, and 5

# pick item 2
C = 2
total_val = 3

# we can only choose item 5 now, since its weight = 2
C = 0
total_val = 5

# what if we picked item 3 instead of item 2?

# pick item 3 after picking item 1
C = 1
total_value = 6

# we can see that picking item 1 -> item 3 gets us
# a total value of 6, and a total weight of 6.
# since C = 1, we can't choose any other items 
```

Now, what if we chose to pick `items[2]` first?
``` python
# C = 7 - 1 
C = 6
# total_val = 0 + 2
total_val = 2

# pick item 3
C = 3
total_val = 6

# pick item 5 (only one we can pick)
C = 1
total_val = 9

# instead of picking item 3, let's pick item 4
C = 6 - 4 = 2
total_val = 2 + 5 = 7

# since we have a capacity of 2 left, we can
# only choose item 5 (again)
C = 2 - 2 = 0
total_val = 7 + 3 = 10

# we reached our globally maximum possible value
```

Did you notice the overlapping subproblems?

We are choosing items based on a current capacity, which is the difference of the given capacity and the weights of the items chosen. Also notice how, at each current capacity, there's a selection of items that maximizes the value (i.e. for both examples, when `C = 2`, we see that `item[5]` maximizes the total value for that capacity) 

Thus, at each choice, *we're choosing the local maximum value possible at some weight `c <= C`*, which is our **subproblem**.

### Problem visualization 
Let's run through the previous example with a visualization. For this, we'll be using a **dynamic programming table**, which is pretty much our memoization table.

Each row represents the items that we *consider* from `1` to some item `j`. Each column represents the **total current capacity**.

Thus, each entry represents the **current maximum value** we can contain in our knapsack within the capacity (from `0` to `7`) when we consider items from `1` up to `j`. Essentially, each entry represents a subsolution.

Here's an uninitialized memoization table.

|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|---|
| **0** |   |   |   |   |   |   |   |   |
| **1** |   |   |   |   |   |   |   |   |
| **2** |   |   |   |   |   |   |   |   |
| **3** |   |   |   |   |   |   |   |   |
| **4** |   |   |   |   |   |   |   |   |
| **5** |   |   |   |   |   |   |   |   |

Here are the values we're working with:
``` python
items = [(0, 0), (2, 3), (2, 1), (4, 3), (5, 4), (3, 2)]
```

First, we consider all the possibilities if we consider `0` items, with a capacity of `0`. It's kind of obvious what the answer is for this one, so I won't explain it.
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** |   |   |   |   |   |   |   |   |
| **2** |   |   |   |   |   |   |   |   |
| **3** |   |   |   |   |   |   |   |   |
| **4** |   |   |   |   |   |   |   |   |
| **5** |   |   |   |   |   |   |   |   |

Now, we consider subcapacities from `0` up to `7` when considering only `items[1]`. If our capacity is `0`, then we can't fit anything in, so the maximum possible value is `0`. This the same for subcapacities `1` and `2`. 

However, for subcapacity `3` to `7`, we can fit `items[1]` into our knapsack. Since we don't have anything else to consider, we can only fill our bag with `items[1]`.
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 |
| **2** |   |   |   |   |   |   |   |   |
| **3** |   |   |   |   |   |   |   |   |
| **4** |   |   |   |   |   |   |   |   |
| **5** |   |   |   |   |   |   |   |   |

We're now considering `items[1]` and `items[2]`. `item[2]` has a weight `w = 1`, so we can fill in our tables for subcapacities `1, 2`, but not `3`. As for `4, 5, 6, 7`, we can see that both items meet or go under those subcapacities, so we can fill them in accordingly.
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4 |
| **3** |   |   |   |   |   |   |   |   |
| **4** |   |   |   |   |   |   |   |   |
| **5** |   |   |   |   |   |   |   |   |

Let's add `items[3]` to our list of items to consider. It has a value of `v = 4` and a weight `w = 3`. Our table won't change for `1, 2`, but notice how `items[3] = (4, 3) > items[1] = (2, 3)`. Thus, we update the maximum possible value at subcapacity `c = 3` to `4`. 

Likewise, for `c = 4`, we get `items[2] + items[3] = 2 + 4 = 6 > 4`, so we update our values for `c = 4`. 
Notice that this is also the case for `c = 6`, where `items[1] + items[3] = 2 + 4 = 6 > 4`.

For `c = 7`, notice how the weights for `items[1], items[2], items[3]` add up to `7`, where `items[1] + items[2] + items[3] = 2 + 2 + 4 = 8 > 6`
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4 |
| **3** | 0 | 2 | 2 | 4 | 6 | 6 | 6 | 8 |
| **4** |   |   |   |   |   |   |   |   |
| **5** |   |   |   |   |   |   |   |   |

Adding `items[4]` into our consideration list, where `items[4] = (5, 4)`, we have a new value for `c = 5, 6`, which is `items[2] + items[4] = 2 + 5 = 7 > 6` (total weight `w = 5`). 

For `c = 7`, we have `items[3] + items[4] = 4 + 5 = 9 > 6`.
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4 |
| **3** | 0 | 2 | 2 | 4 | 6 | 6 | 6 | 8 |
| **4** | 0 | 2 | 2 | 4 | 6 | 7 | 7 | 9 |
| **5** |   |   |   |   |   |   |   |   |

We're on the final row now, where we choose `items[5] = (3, 2)`. Let's get a little bit more specific as to how we should intuitively choose how to update our maximum values at each subcapacity.

For `0` to `1`, our values remain the same.  

If we pick `items[5]` when `c = 2`, our new capacity is `c = 2 - 2 = 0`, which gives us `0 + 3 = 3 > 2`, so we update.

If `c = 3`, and we choose `items[5]`, our new capacity is now `c = 3 - 2 = 1`, and the maximum value when `c = 1` is `2`. Since `3 + 2 = 5 > 4`, we update our maximum value when `c = 3` from `4` to `5`.

For `c = 4`, and we choose `items[5]`, `c = 4 - 2 = 1`. The maximum capacity at `c = 1` is `2`, but `3 + 2 = 5 < 6`, so we don't update anything.

When `c = 5`, and we choose `items[5]`, `c = 5 - 2 = 3`, and the maximum value for `c = 3` is 4, and since `4 + 3 = 7 = 7`, we don't really have to update anything.

Now, when `c = 6` and we choose `items[5]`, `c = 6 - 2 = 4`, where the maximum value for `c = 4` is `6`. Since `6 + 3 = 9 > 7`, we update the maximum value at `c = 6`.

Finally, when `c = 7` and we choose `items[5]`, `c = 7 - 2 = 5`. The maximum value when `c = 5` is 7, and since `7 + 3 = 10`, we update the entry when `c = 7`, and thus reach our global maximum value.

|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7     |
|-------|---|---|---|---|---|---|---|-------|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0     |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2     |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4     |
| **3** | 0 | 2 | 2 | 4 | 6 | 6 | 6 | 8     |   
| **4** | 0 | 2 | 2 | 4 | 6 | 7 | 7 | 9     |
| **5** | 0 | 2 | 3 | 5 | 6 | 7 | 9 | **10** |

Our maximum value when considering all `5` items with the total capacity `7` is therefore `10`.

#### Intuition and subproblems (revisited)
Now that we ran through a visualization of how the memoization table is built, what subsolutions and intuitions did you notice?

**Subproblems and subsolutions**: 
We previously defined the subproblems as the local maximum value we can have with a current subcapacity. 

The solutions we derived were done by computing each maximum value for each subcapacity by considering `1, ..., j <= n` items. We did this by, when considering the item `j`, subtracting `C - w_j`, then looking at the maximum value available at that subcapacity (see traceback for when `j = 5`).

**Intuition**:
We build up a memoization table by considering the subproblem, then incrementally solving each of those subproblems to build up an overall solution.


## Solution
Let's derive a recurrence for how to choose when to replace an item with another one. Let `V(j, w)` be the current maximum value when considering `j` items with a current subcapacity of `w`. 

When do we choose to keep things the same and when do we choose to update?

1. **Keep things as is**: When our weight for item `j`, `w_j`, is greater than our current subcapacity `w`, we can't add item `j` to our knapsack. Thus, we don't do anything.
2. **When to update**: If we can add item `j`, where `w_j` is the weight and `v_j` is the value, we first check the max. value for subcapacity `w - w_j` when considering `j - 1` items, taking the max between the new sum or the original maximum value.

Thus, we get a recurrence:
![recurrence](https://i.imgur.com/fpXYdsU.png)

## Optimal substructure
As a reminder, a problem of size *n* has an optimal substructure if its global solution can be built from subsolutions to subproblems of size *n' < n*. Based on this definition, can you guess what the optimal substructure to this problem is? 

Looking at how we build our [solution table](#problem-visualization), we can see how the optimal substructure works as the algorithm continues to run.

More specifically, the optimal substructure lies in our recurrence, or in other words, how we decide *when* to update which items to put into the knapsack:

``` python
# Max value sum when considering items 1, ..., j  at current weight capacity w
V[j][w] = max(V[j - 1][w], V[j - 1][w - w_j] + v_j)
```

Our optimal substructure lies in how we solve our overlapping subproblems, which are the maximum value we can have in a knapsack with a subcapacity `w <= C` when considering items `1, ..., j <= n`. Let's redefine our **overlapping subproblems** first.

We solve our subproblems by solving for all possible weight capacities from `0` to `C` when considering `items[1]`, `items[1:2]`, ..., `items[1:n]`. 

When we want to consider a new maximum value at some capacity `w` by choosing from items `items[1:k]` (`k <= n`), we first compute the maximum value possible if we choose to put `items[k]` into the knapsack using our recurrence. We do so by adding the value of `items[k]` to the maximum possible value when considering `items[1:k - 1]` at a subcapacity `w - w_j`. This way, we're solving for the subproblem by solving a smaller subproblem, which is the maximum value in our knapsack at some smaller subcapacity `w' < w` when considering items `1, ..., k - 1`. *This* is how our **optimal substructure** is formed - we use previous solutions to smaller subproblems to solve other subproblems, which in turn builds up to the global solution.

To contextualize this, let's use our previous [example](#problem-visualization) (`C = 7` and `n = 5`) and try to solve for the maximum value we can have at `w = 6` when considering `items[1:5]`:

|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7     |
|-------|---|---|---|---|---|---|---|-------|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0     |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2     |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4     |
| **3** | 0 | 2 | 2 | 4 | 6 | 6 | 6 | 8     |   
| **4** | 0 | 2 | 2 | 4 | 6 | 7 | 7 | 9     |
| **5** | 0 | 2 | 3 | 5 | 6 | 7 | <span style="color:red">X</span>  |       |

Here's the value and weight for `items[5]`

``` python
items[5] = (v[5] = 3, w[5] = 2)
```

If our current capacity is `w = 6` and we choose to put `items[5]` into our knapsack, then its weight reduces our current capacity to `w = 6 - 2`, making `w = 4`. Since we already added `items[5]`, then we can only choose from `items[1:4]`.

This is where our optimal substructure comes into play. If you look at the table, we already solved the smaller subproblem where we compute the maximum value possible when considering `items[1:4]` at the capacity `w = 4` (highlighted in green):

|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7     |
|-------|---|---|---|---|---|---|---|-------|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0     |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2     |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4     |
| **3** | 0 | 2 | 2 | 4 | 6 | 6 | 6 | 8     |   
| **4** | 0 | 2 | 2 | 4 | <span style="color:green">6</span> | 7 | 7 | 9     |
| **5** | 0 | 2 | 3 | 5 | 6 | 7 | <span style="color:red">X</span>  |       |

This brings us to the solution to our current subproblem, which is the maximum value we can get when adding `items[5]` to our knapsack when `w = 6`:

``` python
# maximum value when considering items[1:4] at w = 4
V[4][4] = 6
# current maximum value when choosing items[5] at w = 6
curr_val = V[4][4] + 3 = 6 + 3 = 9
```

This `curr_val` is *greater than* our other previous subproblem, which is the maximum possible value when considering `items[1:4]` at `w = 6`:

``` python
V[4][6] = 7
```

Thus, we get a new **optimal solution** `V[5][6] = 9` to the subproblem when our weight capacity is `w = 6` (highlighted in red):

|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7     |
|-------|---|---|---|---|---|---|---|-------|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0     |
| **1** | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2     |
| **2** | 0 | 2 | 2 | 2 | 4 | 4 | 4 | 4     |
| **3** | 0 | 2 | 2 | 4 | 6 | 6 | 6 | 8     |   
| **4** | 0 | 2 | 2 | 4 | <span style="color:green">6</span> | 7 | 7 | 9     |
| **5** | 0 | 2 | 3 | 5 | 6 | 7 | <span style="color:red">9</span>  |       |

If we continue onto the next step, we'll be using the optimal substructure to solve for the *globally* optimal solution `V[5][7]`.



