# Closest Pair of Points
Consider a set of points `P`, represented as a list of tuples `(x[i], y[i])` that contains elements from two lists of x-coordinates and y-coordinates, called `x` and `y`.

Our goal is to determine the pair of points in the list `P` with the *minimum* Euclidean distance between them. In other words, fine the shortest line made from the points.

Assume that `P` is bijective, meaning that no `x[i]` and `x[j]` can be the same, but all points in `x` and `y` can be mapped to each other. 

To visualize (closest pair highlighted in red):

![point-plane](https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Closest_pair_of_points.svg/440px-Closest_pair_of_points.svg.png)

This problem is a *little* bit trickier than our previous problems, which were basically variations of each other.

Side note:
``` python
dist = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
```

### Division
Let's think of a way to divide our problems first, before defining the subproblems.

How *good* is dividing the region of points into a four quadrant Cartesian plane?

![cartesian-plan](https://i.imgur.com/1ox1X2O.png)

Looks like it's pretty good! There's one problem though... what if our points only lie in, say, one or two quadrants? Or if the points aren't evenly distributed throughout?

![cartesian-plan-fault](https://i.imgur.com/t5p8qzw.png)

We can see that dividing the region into four quadrants doesn't work very well. So, it makes sense to divide the region into two subregions with a line `L` s.t. the points are somewhat equally distributed:

![half-region](https://i.imgur.com/7R2Qizw.png)

### Conquer
This way, we can recursively find the closest pair of points in each respective region, then compare `min(line1, line2)`.

![respective-pairs](https://i.imgur.com/EUytcdP.png)

### Combine
Notice how, in the previous picture, there's actually a pair of points that make a shorter line than `line1` and `line2`:

![new-pair](https://i.imgur.com/2vU59wu.png)

So, now comes our **combine** portion.

We can find the closest pair of points *between* the regions by limiting our search space to the length of the shortest line in the horizontal direction across both gradients. This means that, if we detect a line within this region, it'll be shorter than the line we previously found.

To visualize:

![partition-inbetween](https://i.imgur.com/wMg5A4n.png)

Note that we don't have to compare the points along the same side of the gradient, since those lines would have been found by our **conquer** part of our algorithm.

If we sort each point within the boundaries by their y-coordinates, all we have to do is compare the points that appear *across* the gradient. 

![sorted-y](https://i.imgur.com/hRVafqt.png)

For example, we have *5* points on one side of the gradient, and *2* on the other. We just have to compare all *5* points to the other *2* points.

All we have to do at this point is find the min. pair, which we'll call `line`, across the gradient `L`, then return `min(min(line1, line2), line)`.

## Algorithm
Let `x` be a list of x-coordinates, and `y` be a list of y-coordinates.

`P` is a list containing points, represented as the tuple `(x[i], y[i])`.

Below is a divide and conquer algorithm that finds the closest pair of points in `P`.

``` python
# assume that we can access x and y from this method
def closest_pair(P):
    # len(P) = len(x) = len(y) im pretty sure
    n = len(P)
    # partition into two regions
    mid = n / 2
    L = P[:mid]
    R = [mid:]

    # get closest pairs
    line1 = closest_pair(L)
    line2 = closest_pair(R)
    # min pair between gradient 
    line_LR = min(line1, line2)
    # remove all points out of bounds line_LR
    P = [P[x] for x in range (n) if P[x] < line_LR]
    # sort y-coordinates
    P = sort_by_ycoord(P)
    # scan points across gradient in y-order
    line = closest_split_pair(P, mid, line_LR)
    # return shortest line
    return min(line, line_LR)

# finds closest pair across gradient
def closest_split_pair(P, L, pair):
    # init default pairing
    line = dist(P[0], P[mid])
    # search through each point
    for i in range(len(P)):
        # search through each point across gradient
        for j in range(L, len(P)):
            p, q = P[i], P[j]
            dst = dist(p, q)
            line = min(dst, line)
    return line



# compute euclidean distance
def dist(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# sort P by y-coordinates
def sort_by_ycoord(P):
    n = len(P)
    # simple bubble sort
    for i in range(n):
        for j in range(n):
            if P[i][1] > P[j][1]:
                P[i], P[j] = P[j], P[i]
    return P
```

Honestly I don't know if this code is correct. I didn't run it. Feel free to check though.



