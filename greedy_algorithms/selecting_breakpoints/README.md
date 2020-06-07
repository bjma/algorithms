# Selecting Breakpoints
Consider the following problem:
> You're planning a road trip from Santa Cruz to Las Vegas, and you're driving a Tesla with a battery life capacity *C*, represented as the distance until our Tesla diesn out. 
>
> Along your roadtrip map, represented as the interval *d = [0, L]*, charging stations are marked with a vertical line. 
> 
> As you drive, your capacity *C* will decrease, but at each charging station, you can recharge your Tesla up to the full capacity *C*.
>
> Your **goal** is to devise an algorithm that minimizes the number of stops you make during your trip.

To visualize:

![roadmap](https://i.imgur.com/eE5eLTi.png)

We have the overall problem. As I mentioned before, now we need to find a subproblem that can be solved with a greedy heuristic, giving us an optimal substructure.

## Greedy heuristic/choice
If we wanted to minimize the number of stops, obviously the greediest heuristic is to go as far as we can *without stopping*. But how do we do this?

Consider the current distance traveled `x` and our current capacity `C`. Which breakpoint should we choose based on those two?

Let some breakpoint `b[p]` be the breakpoint at a point `p`. We need to select a breakpoint when our `C` is going to deplete. This distance before our Tesla dies can be represented as `x + C`.

In other words, we stop at a charging station when: `b[p] <= x + C`

## Optimal substructure
How can we devise the algorithm in a way where our subsolutions form the global solution?

Recall our greedy heuristic of choosing to stop at a charging station when `b[p] <= x + C`.

We can use this to create an optimal substructure **to  force our greedy heuristic to always be optimal**. 

How do we ensure that we don't just randomly choose a suboptimal breakpoint? If we simply just stop whenever `b[p] <= x + C`, then we might make more stops than we need. 

To ensure that this doesn't happen, we should first sort the list of breakpoints `b` s.t. every breakpoint is in increasing order. This doesn't completely solve the overall problem though. We need to do some additional restructuring. 

The key to our optimal substructure is to **pick the largest integer `p` such that `b[p] <= x + C`**.

Thus, we update our current distance `x` to the breakpoint `b[p]` in which we stop at. Then, we append the breakpoint into our subset. If `b[p] = x`, that means `C = 0`, implying that we're out of battery, and our road trip ends prematurely.

## Algorithm
Below is the code for selecting breakpoints:

``` python
# Also called truck driver's algorithm
# Let b be the set of breakpoints
# Let C be the fuel capacity
# Let L be the total distance
def select_breakpoints(C, L, b):
    n = len(b)
    # sort breakpoints in increasing order
    b.sort()

    # init solution set S for appending breakpoints
    S = []

    # init curr. distance x
    x = 0

    # begin our trip
    while (x < b[n]):
        # find breakpoint p s.t. b[p] <= x + C
        p = find_breakpoint(C, x, b)
        # no solution
        if (b[p] == x):
            return [0]
        x = b[p]
        S.append(p)
    return S
```
Here's the code for finding a breakpoint where `b[p] <= x + C`:
``` python
# Return breakpoint p s.t. b[p] <= x + C
# We can use binary search since b is sorted
def find_breakpoint(C, x, b)
    n = len(b)

    # distance until depletion
    dist = x + C

    # get middle index
    p = n // 2

    # split halves to look for max index
    left = find_breakpoint(C, x, b[:p - 1])
    right = find_breakpoint(C, x, b[:p + 1])

    # find breakpoint
    if b[p] < b[left] and b[left] <= dist:
        p = left
    if b[p] < b[right] and b[right] <= dist:
        p = right
    return p

```

