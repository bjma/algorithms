# Segmented Least Squares
This is another dynamic programming problem that uses the technique of **multiway decisions**.

## Least Squares: A summary
Least squares are a foundational problem in statistics.
Consider the following linear model:

![lin_model](https://i.imgur.com/8d2AuoF.png)

The line `y = a*x + b` is a line that fits into our data set (represented as a cluster of points) such that the sum of squared errors between the line and the data points are minimized.

Here's the equation for the sum of squared errors:

![sse](https://i.imgur.com/TprgNDG.png)

This line fits pretty well for a data set that's kind of linear. However, what if we have a data set that can't be accurately approximated using a single, linear model (Ignoring logistic regression)?

The answer is to fit two or more lines to the data set! This way, we have a problem of *segmented* least squares linear model.

![segmented_least_squares](https://kartikkukreja.files.wordpress.com/2013/10/segmented.png?w=300&h=204&zoom=2)

## Problem
The problem is as follows:
> Given a set of points `P = [(x[1], y[1]), (x[2], y[2]), ..., (x[n], y[n])]`, where `x[1] <= x[2] <= x[n]`, partition `P` into segments, where each segment is a contiguous subset of `x`, such that each line formed by such subsets minimize the sum of squared errors.

To put it in simpler terms, minimize the line `f(x) = E + cL`, where `E` is the sum of the sums of squared errors in each segmented line, and `L` is the number of lines.

## Multiway choice
Let `OPT[j]` be the minimum cost (error) for the points `P[1], P[2], ..., P[j]` (points from `1` to `j`).

Let `e[i, j]` be the sum of squared errors for points `P[i], P[i + 1], ..., P[j]`.

To compute `OPT[j]`,
* Last segment uses some points `P[i], P[i + 1], ..., P[j]`.
* Cost = `e[i, j] + c + OPT[i - 1]`