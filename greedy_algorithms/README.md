# Greedy Algorithms
Greedy algorithms is an algorithmic technique similar to divide and conquer, where we define some subproblems. However, instead of dividing our problem into subproblems to solve them individually, we *incrementally* solve each subproblem by choosing a *locally optimal* solution for that subproblem, in order to build a globally optimal solution for the overall problem.

A general definition of a greedy algorithm is:
> A greedy algorithm solves a problem using "greedy" heuristics by making the locally optimal choice at each stage with the intent of finding a global optimum
> -Wikipedia

I really like using the simplification used by Erik Dermaine (MIT):
> "Eat the biggest cookie"
> -Erik Dermaine

## Greedy properties
* Optimal substructure
    * Devise the algorithm in such a way where subproblems yield **locally optimal solutions** that build up to a **globally optimal solution**
* Greedy-choice property (greedy heuristic)
    * Each subproblem is solved using a **locally optimal choice**

## Strategy for definining an optimal substructure
Let's use the problem of [interval scheduling](https://en.wikipedia.org/wiki/Interval_scheduling#:~:text=Interval%20scheduling%20is%20a%20class,it%20needs%20to%20be%20executed.) as an example, which can be solved using a greedy algorithm.

Consider a set of *n* jobs, represented by a start time `s[j]` and finish time `f[j]`, where `1 <= j <= n`:

![interval](https://i.imgur.com/jYG1GyD.png)

Notice how the figure above refers to the compatibility between two jobs. Two jobs,  `job[j] = (s[j], f[j])` and `job[i] = (s[i], f[i])`, are considered **incompatible** if `s[i] < f[j]`, meaning the two jobs *overlap*. If two jobs are *not* incompatible, they are considered mutually compatible.

**Goal**: Find the *maximum* subset of mutually compatible jobs.

Let's try to find an optimal structure to our algorithm. Obviously, the optimal approach is to get some `job[j]` and reject all jobs that are incompatible to `job[j]`. However, we're now dealt the problem of *finding* how to optimally choose each job, which helps gives us the optimal substructure.

Below, I'll go over different optimal choices we can make and compare them.

### Determing an optimal choice for selecting jobs
Let's go over some optimal choices (greedy heuristic) we can make when selecting jobs. This way, if we define an optimal choice, we create an optimal substructure to our subproblems.

Let the set of jobs be a list of tuples containing start times and finish times of each respective job:
 `jobs = [(s[1], f[1]), (s[2], f[2]), ..., (s[n], f[n])]`

#### (a) Select earliest relative start time
Let's say we choose the job with the earliest relative start time, starting with `min_start(jobs)`.

![earliest-start-time](https://i.imgur.com/icLmXKd.png)

We can see that the optimal solution is *4*, which are the jobs above the longest interval. However, since we're selecting the *earliest* start time, we'd choose the longer interval on the bottom. We also reject all incompatible jobs in the process, so the four jobs above are discarded.

Thus, we can conclude that this "optimal choice" isn't optimal at all.

#### (b) Select job with the shortest duration
Correcting what happened with our previous choice, what if we chose the job with the shortest duration?

![shortest-job](https://i.imgur.com/VvYewAz.png)

We can see that this also isn't an optimal choice. The optimal solution is *2*, which contain the two jobs above. If we simply choose the shortest job, we miss out on an optimal solution.

#### (c) Select the least incompatible job
Okay, so what if we choose the job that has the least number of incompatible jobs?

Looking at our previous choices, we can see that choosing the jobs with least incompatibles solves our problems. For **(a)**, all four jobs above the longer one have *1* incompatible jobs, where the long one has *4*. Likewise, the two jobs in **(b)** above the short interval, which has *2* incompatibilites, each have *1* incompatibility.

However, observe this case, where our choice isn't as optimal as we hoped:

![least-incomp](https://i.imgur.com/46BeAKn.png)

Our optimal solution is *4*. but since we choose the least incompatible jobs, but since we're choosing the least incompatible jobs, we choose the first one, then the middle one that has *2* incompatiblities, then the last, giving us a solution of at least *3*. 

Thus, this choice is not optimal.

#### (d) Select job that finishes the earliest
If we select the job that finishes the earliest, or in other words, a job s.t. `job[j] = min_finish(jobs)`, we can solve a lot of the problems we ran into before.

For **(a)**, we'd be able to choose the *4* jobs on top.

For **(b)**, we'd choose the first job, drop the second, and pick the third.

For **(c)**, we'd choose the first, drop the three that stack, pick the fourth, drop the third (middle) one, then pick the sixth job, so on and so forth.

So, this way of selecting jobs seems to be the optimal choice.

### Optimal substructure for interval scheduling
We now found the optimal choice, which is our greedy heuristic. How are our subproblems optimally structured?

We have an optimal substructure if our subsolutions build up to a global solution. So how does our greedy heuristic do this? 

Recall our definition of incompatibility, where two jobs `i` and `j` are incompatible if `s[i] < f[j]`. Our greedy heuristic lies in selecting the relative minimum `f[j]`, so any start time `s[i] < f[j]` is rejected, allowing us to avoid adding any incompatible jobs to our subset. After, we choose another `f[k]`, where `f[k] > f[j]`, and remove all `s[i] < f[k]`. 

*This* is our **optimal substructure** - we basically choose the smallest relative "limit" over the all the jobs, which ensures we choose the maximum number of jobs, while rejecting all incompatible jobs within that small limit.

## Content
The following are the greedy algorithms that we will cover:
* Interval scheduling (we used this as an example above)
* Selecting breakpoints
* Dijkstra's Shortest Paths
* Kruskal's Minimum Spanning Trees
* Prim's Minimum Spanning Trees

## Summary
In essence, we can build a greedy algorithm by sticking to the follwoing general strategy:
* Define **subproblems**; usually done by finding an **optimal approach**
* Determine a **locally optimal choice** for the subproblems such that it provides an **optimal substructure** (a substructure of the original problem that ensures our optimal choice is always optimal) 
* Use that optimal substructure to build a **globally optimal solution** from **optimal subsolutions**







