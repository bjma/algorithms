# Kruskal's & Prim's
>Before continuing on with this section, be sure to review the notes on [graphs](https://github.com/bjma/cse-102/tree/master/resources/graphs/README.md) if you aren't comfortable with them.

There are two algorithms that find the **minimum spanning tree** (MST) for a connected weighted graph.

We'll be comparing both **Kruskal's algorithm** and **Prim's algorithm** since they're different implementations of the same problem.

## Minimum Spanning Tree
A minimum (weight) spanning tree (MST) is the subset of edges `E'`of a connected undirected weighted graph `G` such that *all* vertices in `V` are connected to each other with the *minimum sum of total edge weight*. Since it's a tree, that means the subset of edges must not form a cycle.

To visualize, here's a graph with its MST highlighted:

![mst](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Minimum_spanning_tree.svg/600px-Minimum_spanning_tree.svg.png)

## Kruskal's Algorithm
Kruskal's algorithm makes an **optimal choice** by iteratively choosing each edge `e` with the *least* relative edge weight, pushing `e` to our solution set `S` if it doesn't create a cycle in `S`. If the current cheapest edge `e` forms a cycle in our current MST, we discard `e` from `G` and move on to the next cheapest edge.

### Optimal substructure
To ensure that we're always choosing the cheapest edge at each stage, we form an optimal substructure by sorting the set of edges `E` in increasing order of edge weight.

### Algorithm
I won't actually include `.py` files this time. However, feel free to check online for different implementations.

``` python
# G = (V, E)
def kruskals(G):
    # solution set for MST
    S = []
    # get vertices
    V = G[0]
    # get edges represented as vertex pairs; each edge has an associated weight value
    E = G[1]
    # sort edges in ascending order
    E.sort()

    for (u, v) in E:
        # if the edge does not form a cycle
        if parent(u) != parent(v):
            S.append(E.dequeue())
        else:
            E.dequeue(u, v)
    return S
```

## Prim's Algorithm
Kruskal's algorithm builds an MST by sorting the edges in increasing order of weight, then iteratively choosing each edge that doesn't create a cycle.

In contrast, Prim's algorithm starts at some arbitrary source vertex `s`, iteratively building an MST by traveling from node to node, considering the edge candidates for each node `v` and choosing the one with the least weight that also doesn't create a cycle.

### Edge candidates
Prim's algorithm uses something like a "field of view" when traveling from vertex to vertex, consisting a set of all possible edge candidates. 

For example, when we start at the source vertex `s`, our current edge candidates are all adjacent vertices to `s`. We choose the minimum weight edge out of all of the candidates so long as it doesn't form a cycle, and do the same for the next node. Upon traversing to a node, the set of edge candidates is expanded.

To visualize, refer to the figure below, which is Prim's algorithm at the stage where we go from `A` to `B`. The edge candidates are bolded, and the chosen candidate is highlighted in green.

![prims1](https://i.imgur.com/aww8KAH.png)

At this point, we choose the min. cost edge, which is `C` (we can also choose `D`, but we do it in order of the set of edge candidates):

![prims2](https://i.imgur.com/2y4Ywj1.png)

As you can see, we expand our available choices for edges that construct an MST. This is our optimal substructure.

### Optimal substructure
Our optimal substructure here is that we have a list of edge candidates we can choose from that increases at each vertex traversal. This way, we ensure our **greedy heuristic** of choosing the min. cost edge is always optimal by choosing the candidate with the least edge weight that doesn't form a cycle.

### Algorithm
Here's the pseudocode for Prim's: 

``` python
# Let s be some source vertex
# Let G = (V, E)
#
# Let get_neighbors(v) be a method that returns 
# neighbors of v as a list
#
# Let compute_edges(u, V) be a method that 
# returns a list of computed (u, v) edge pairs 
# from a set of vertices V, where V[i] = v
#
# Let forms_cycle(u, V) be a method that
# returns True if u forms a cycle with any vertex in V
def prims(G, s):
    # solution set
    S = []
    S.append(s)
    # edges and vertices
    V = G[0]
    E = G[1]
    # candidates as vertices starting at source
    candidates = [v for v in get_neighbors(s)
    # set current vertex as source
    v = s
    # construct MST until we connected all vertices
    while len(S) != len(V):
        # choose next min. weight edge candidate
        v = min(compute_edges(v, candidates))
        # check if our vertex forms a cycle
        if not forms_cylcle(v, candidates):
            # add v to our solution
            S.append(v)
            # expand candidates
            candidates.append([u for u in get_neighbors(v)])
        else:
            # discard vertex
            V.remove(v)
    retrurn S
```