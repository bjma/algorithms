# Knapsack Problem
The [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) is a pretty famous interview problem that uses dynamic programming. 

There are two variations, the simple Knapsack problem (where you can use a greedy heuristic to solve the problem), and the 0-1 Knapsack problem, which forces you to either *choose* or *not choose* to collect an item (binary choice).

## Problem
Imagine that you are a robber breaking into a house to steal some items. You are carrying a knapsack with a maximum weight capacity `C`, and can choose any number of items with an associated weight `w` and value `v`, so long as the total weight of the items you chose don't exceed the capacity `C`.

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

Thus, at each choice, *we're choosing the local maximum value possible at some weight `c <= C`*, which is our subproblem.

### Problem visualization 
Let's run through the previous example with a visualization. For this, we'll be using a **dynamic programming table**, which is pretty much our memoization table.

Each row represents the items that we *consider* from `1` to some item `j`. Each column represents the **total current capacity**.

Thus, each entry represents the **current maximum value** we can contain in our knapsack within the capacity (from `0` to `7`) when we consider items from `1` up to `j`.

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| 0 |   |   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |   |   |
| 3 |   |   |   |   |   |   |   |   |
| 4 |   |   |   |   |   |   |   |   |
| 4 |   |   |   |   |   |   |   |   |