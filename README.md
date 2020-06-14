# Algorithms :book:

This repository contains notes on algorithm design strategies and some common algorithms covered in university textbooks. 

All solutions and implementations are written in Python.

## Introduction
In Spring 2020, I took my university's Intro to Algorithm Analysis & Design course. I struggled a lot in this course - wrapping your ahead around the different approaches to writing algorithms came slowly to me.

The weekend before finals week, I decided to write up this entire repository of notes to review, using my professor's lecture slides as reference. In the end, I think I came out understanding this stuff pretty well.

I'm leaving this repository public for any other students who also struggle with this material, in hope that you guys see how cool this stuff is to learn.

## Why algorithms?
A lot of computer science students dread the inevitable moment when they take their first algorithm class. The material is notoriously difficult to digest, and actually having to implement these algorithms is nerve-wracking.

So why learn them?

Although you'll probably never have to write an actual groundbreaking algorithm as a software engineer, but knowing different algorithm design strategies is especially important when you're going to be writing efficient code.

Think about this - how would you sort an array of numbers? The naive approach everyone learns is the *brute force* method - compare each element at an index with each and every other element at other indices:

``` python
def sort(A):
    n = len(A)
    for i in range(n):
        for i in range(n - i):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
    return A
```

The thing is, this brute force way of sorting is inefficient. For small arrays, the speed doesn't make that much of a difference. However, if our arrays were size, say, *1000*, sorting using this method takes a long time.

One algorithm strategy that sorts an array much faster than this brute force method is divide and conquer (namely, [merge sort](https://github.com/bjma/algorithms/tree/master/divide_and_conquer/merge_sort)).

As a software engineer, you'll be required to write efficient, scalable code. To do this, having an understanding of algorithm design is essential. Not only that, technical interviews for software engineering positions involve the algorithmic strategies in this repository.

The biggest thing to take away from the materials I'm providing is that there are many different strategies to solve algorithm problems which don't involve brute force.

## Content
* Divide & Conquer
* Greedy Algorithms
* Dynamic Programming
* Resources
    * Runtime analysis (Big O, recurrence relations)
    * Graph theory crash course

