# RNA Secondary Structure
RNA is an abbreviation of ribonucleic acid. Honestly, I don't know anything about this concept beyond basic biology from high school, but for the sake of this problem, let's consider it as a sequence of strings.
![rna structure](https://i.imgur.com/smeeoqf.png)

As you can see, if we go from right to left, starting at `G`, we get the string displayed at the bottom of the image.

RNA is composed of bases, namely guanine, adenine, uracil, and cytosine. Each base has a complementary pair called a **base pair** (shown in the image above). If we were to list all the bases and their complements, it would look something like a hashmap:
``` python
rna_base_pairs = {
    A : U,
    G : C,
    C : G,
    U : A
}
```

A set of pairs `S = [(b_i, b_j)]`, where `b_i` and `b_j` are bases, must satisfy the *Watson-Crick* complement (where we represented as a hashmap above).

## Secondary structure
Consider the RNA sequence `B = "AUGGGGCAU"`. We must determine a set of pairs that match each base with its complement.

![ex. 1](https://i.imgur.com/AvSlvef.png)

Let's represent it as a string:
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|----|
| A | U | G | U | G | G | C | C | A | U  |

Take note of the *structure* of the RNA sequence. Each pair is made from both ends of the sequence (`A-U`, `U-A`, `G-C`). 

A possible set of pairs that satisfy *Watson-Crick* would be
``` python
S = [(b[1], b[10]), (b[2], b[9]), (b[3], b[8])]
# after this point, the rest of the sequence is just G,
# which are incompatible with each other
```

Note some caveats that we need to keep track of:
* (No sharp turns) - The ends of each pair are separated by *at least* 4 intervening bases (in this case, it's `U-G-G-C`). Thus, for a pair `(b[i], b[j])` in `S`, `i < j - 4`.
* (Non-crossing) - If the pairs `(b[i], b[j])` and `(b[k], b[l])` are in `S`, then we can't have `i < k < j < l`
    * For example, for the pairs `(b[1], b[10])` and `(b[2], b[9])`, notice how `j = 10 > l = 9`.

All of these caveats, and a set of pairs satisfying the *Watson-Crick* complement, forms the RNA secondary structure.
### Free-energy hypothesis
> RNA molecule will form the secondary structure with the minimum total free energy

Consider the approximation: more base pairs = lower free energy.

## Goal
Our goal is to, for an RNA sequence of bases represented as a string, `B = "b[1] b[2]... b[n]"`, determine a set `S` of base pairs that satisfy the *Watson-Crick* complement, such that we have an RNA secondary structure that maximizes the number of pairs in `S`.

## Intuition and subproblems
Let `OPT(i, j)` be the maximum number of base pairs in a secondary structure substring `b[i] b[i + 1] ... b[j]`.

### Case 1
If `i >= j - 4`, `OPT(i, j) = 0` (no sharp turns)

### Case 2
If `b[j]` is not in a pair (i.e. cannot be paired with any base from `i` to `j - 1`), `OPT(i, j) = OPT(i, j - 1)`. 

In other words, reduce our search range.

### Case 3
If `b[j]` pairs with some `b[t]` for some `i <= t < j - 4`, then 
`OPT(i, j) = max(OPT(i, j - 1), 1 + max(OPT(i, t - 1) + OPT(t + 1, j - 1)))`, 
where `OPT(t, j) = 1`.   

To understand this part, recall the non-crossing caveat, visualized here:

![non-crossing](https://i.imgur.com/b435Aiq.png)

Thus, if `b[j]` pairs with some `b[t]` where `i <= t < j - 4`, then notice how we're confined the the bounds `i` to `t - 1` since we can't have any crossing pairs:

![bounds](https://i.imgur.com/IN27H4w.png)

So, we're faced with two independent subproblems: finding a sequence within the bounds of `i` to `t - 1`, and `t + 1` to `j - 1` if `b[t]` and `b[j]` match.