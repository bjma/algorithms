# Dijkstra's Shortest Paths
Before continuing on with this section, be sure to review the notes on [graphs](https://github.com/bjma/cse-102/tree/master/resources/graphs/README.md) if you aren't comfortable with them.

Perhaps the most famous problem in computer science, **Dijkstra's algorithm** finds the shortest path from a source vertex `s` to all other vertices in a directed weighted graph `G = (V, E)` (or a destination node `t`), where `len(V) = n`.

![dijkstras](https://i.imgur.com/WbF3aaX.png)

## Algorithm
Dijkstra's algorithm uses some book-keeping to determine the shortest paths from `s` to `t`, or all other nodes. Namely, we keep information regarding:
* Maintain a set of unvisited nodes `Q` for us to explore
* An array `d` of size `n` containing the current shortest distance from source `s` to some vertex `v`
    * `d[s] = 0`
    * `d[v] = inf` upon initialization for all `v` in `V`
* An array `parent` of size `n` containing the preceding node to some vertex `v` on the current shortest path from `s`
    * `parent[s] = NULL` 
    * `parent[v] = NULL` upon visualization

The steps for the algorithm is as follows:
* Input: graph `G` as adjacency matrix, source node `s`
* Initialize `Q`, `d`, and `parent`
* Repeatedly choose unexplored node `v` from `Q`
* For all unexplored neighbors `u`, compute `d[v] = min(d[v], d[u] + edge_weight(u, v)` to compare two paths
* Set `parent[v] = u` if `u` yields a new shortest path

## Why greedy?
You may be wondering why Dijkstra's algorithm is considered a greedy algorithm. If you looked at the high-level algorithm above, you may notice a locally optimal choice we're making.

Our greedy heuristic is that, starting at some vertex `v` in `Q`, we search through all adjacent nodes `u` to `v` and update `d[v]` if going from `u` to `v` yields a more optimal solution than a previously established shortest path.

But how is this algorithm written in a way where we have an optimal substructure?

### Optimal substructure: Priority Queues
We previously defined `Q` as a set of unvisited nodes that we start at in order to traverse the graph `G`.

If we simply just had the nodes appended in numerical order, we don't really have an optimal substructure, since we're thoughtlessly choosing one vertex to another.

However, if we sorted `Q` in such a way where each vertex `v` in `Q` is in increasing order of *distance* from `s`, we always choose the relative closest vertex from `s` as the first and next vertex we explore. Thus, we always ensure that we'll be finding a local shortest path.

How do we do this, since we don't know which vertices are closer before we run the algorithm?

The key is to use a [priority queue](https://www.programiz.com/dsa/priority-queue), which sorts its elements by a defined priority. In this case, our priority is the minimum distance from `s`.

Priority queues use a data structure called a [heap](https://www.geeksforgeeks.org/heap-sort/). Essentially, each time we add some element to the priority queue `Q`, we insert it into a binary search tree, and *heapify* it so that the heap is rearranged to maintain a binary search tree structure.

To visualize:

***1. Insert new element at end of the tree***
![heap-add](https://cdn.programiz.com/sites/tutorial2program/files/insert-1_0.png)

***2. Heapify the tree***
![heapify](https://cdn.programiz.com/sites/tutorial2program/files/insert-2_0.png)

So, we start with a min-priority queue `Q` that sorts vertices `v` in `V` using our initial values. During the algorithm, we extract the first element `v` in `Q` (FIFO) and determine the shortest path to all adjacent vertices `u`. If `u` yields a shorter path to `v` than another adjacent vertex, then we insert `u` into `Q` and it'll heapify our priority queue for us.

This way of selecting vertices is what gives us our optimal substructure to this problem.

## Algorithm (revisited)
I won't write the entire algorithm for Dijkstra's, but I can provide Pythonic pseudocode for contextualization. If you want to check out the actual code, I included a `.py` file with code from [Programiz](https://www.programiz.com/dsa/dijkstra-algorithm#python-code).

``` python
# Let G = (V, E)
# Let s be the source vertex
def dijkstras(G, s):
    # get the set of vertices from tuple
    V = G[0]
    n = len(V)
    # init min-priority queue Q sorted by min. dist
    Q = [v for v in V if v != s]
    # init book-keeping arrays
    d = [float('inf')] * n
    parent = [None] * n
    d[s] = 0
    
    # while Q is not empty
    while Q:
        # extract min. from Q
        u = Q.delete()
        # implicit method for getting neighbors of input vertex as a list
        neighbors = get_neighbors(u)
        for v in neighbors:
            # get dist from u to v
            dist = d[u] + edge_weight(u, v)
            # update min. dist 
            if dist < d[v]:
                d[v] = dist
                parent[v] = u
                # update d[u] in Q
                Q.insert(u)
    # return min. dist from s to all nodes and parents
    return d, parent
```

What's the runtime for Dijkstra's? If we look at our code, we go through all vertices `V`, which is stored in `Q`. Dequeuing from `Q` thus takes *O(logV)*, since we also need to heapify after both dequeuing and enqueuing. Additionally, we look at all adjacent neighbors to `u = Q.delete()` for all `u`, which means we look at all of the edges, taking us a total of *O(E)*. Since this is all in one loop, the runtime is therefore *O(E logV)*.

### Traceback
The point of having an array `parent` is so that we can form a **shortest path tree**, which displays the shortest path from `s` to some destination vertex `v`:

![spt](https://www.baeldung.com/cs/wp-content/uploads/sites/4/2020/01/dijkstra.jpg)

In this case, the destination vertex `v` is the node `G`. However, in our code above, we constructed a shortest path tree from `s` to *all* the vertices in `G`. This is actually called a **minimum spanning tree** (MST).



