# Dynamic Programming
Dynamic programming is an algorithmic technique that uses mathematical optimization. It's specifically useful for any problem that contains *reoccurring subproblems*.

Dynamic programming problems typically fall within these two realms:
* Combinatorics (counting)
* Minimizing or maximizing a value

## Solving DP problems: An outline
* Define a collection of subproblems
* Build a general solutions by computing subsolutions to subproblems
* Natural ordering of subproblems from 'smallest' to 'largest' enables determining a solution to some subproblem from computing smaller subproblems (clearest example is knapsack)

## DP techniques
* Binary choice (weighted interval scheduling)
* Multiway choice (segmented least squares)
* Adding a new variable (knapsack; we added `V[j, w]`)
* Intervals (RNA secondary structure)