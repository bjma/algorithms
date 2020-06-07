# Divide and Conquer
Divide and conquer, in strategy, is a technique to gain and maintain power.

In terms of algorithms, the definition follows a similar one to the one I mentioned earlier. Given a problem that can be broken down into two or more subproblems of the same type (usually on a smaller scale), we can solve each subproblem to arrive at our desired global solution.

Divide and conquer algorithms follow this general algorithmic strategy:
* **Divide** - Partitioning problem into subproblems
* **Conquer** - Solve each the subproblems, then **combine** them to form the overall solution

## Strategy
The general strategy first is to identify any subproblems that our original problem contains. This usually deals with detecting base cases, which could be a subproblem to our subproblems. I'll explain what this means later on below.

For example, consider the [Tromino Grid Filling](https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/) problem, where you are tasked with filling an *n x n* grid with one gap using a tromino shape that can be rotated freely, where *n = 2<sup>k</sup>* (i.e. *n* is a power of 2) and *k >= 1*.

![tromino-grid](https://i.imgur.com/dn1QSWG.png)

Notice how, if our grid is *2 x 2*, filling a tromino in that space will leave one gap, distinguised by a darker shade of blue:

![tromino-4x4](https://i.imgur.com/UMI0eSj.png)

Our original grid contains a gap, so technically it's okay if we leave a gap in this subproblem. Thus, we solved one of the subproblems, which is filling in a *2 x 2* grid. However, if we can't divide the grid into *2x2* subgrids easily, and it's extremely inefficient. What we need to do now is find a way to get to this subproblem.

We defined a base case (smallest case where our problem can be solved), but we haven't defined a good subproblem yet. What if we widen our scope in how we divide the grid?

Notice how the problem defines *n = 2<sup>k</sup>*, indicating that our dimensions are always squared powers of *2*. We can use a little bit of math to find our subproblems. If we **divide** our *n x n* grid into four equal parts, which is basically dividing the grid in half in the horizontal and vertical axes, we basically divide *n / 2 = 2<sup>k</sup> / 2 = 2<sup>k - 1</sup>*. Since *k >= 1*, this implies that our exit clause (no solution, so return) is *2<sup>1 - 1</sup> = 1* when dividing each axis into half. 

We've now determined 3 things:
* When a grid is *2 x 2*, we solve our problem by placing the tromino anywhere (base case)
* Our exit clause is a *1 x 1* grid
* Dividing a *2<sup>k</sup> x 2<sup>k</sup>* grid into 4 equal parts brings us to a base case

All we have to do is simply place a tromino in the middle of an unpartitioned grid s.t. it leaves a gap in the area where the black gap resides:

![tromino-1](https://i.imgur.com/p7zDNGR.png)

Then **divide** our grid into 4 parts, placing a tromino in the middle of each partition in a similar fashion to how we did before (**conquering**):

![tromino-2](https://i.imgur.com/2tL6iAF.png)

Eventually we'll reach our aforementioned base case of a *2 x 2* grid, eventually filling it out like so (this is our **combine** part of divide and conquer):

![tromino-3](https://i.imgur.com/4kRP195.png)

And thus we solved our problem by solving subproblems and combining them.

## Content
I'll be providing notes on algorithms that we went over in class. This includes:
* Merge sort
* Counting inversions
* Closest pair of points
* Fast Fourier Transform

Just for reference, *Binary Search* is also a divide and conquer algorithm.

## Summary
In essence, to devise a divide and conquer algorithm, we first need to find the base cases, i.e. exit clauses and the smallest possible subproblems.

Then, we need to find a way to **divide** our problem until we reach those subproblems.

After, we **conquer** by solving each subproblem.

Finally, we **combine** all our subsolutions to form the global solution.