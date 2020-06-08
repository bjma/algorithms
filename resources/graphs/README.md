# Graphs
In computer science, graphs are an abstract data type that implement graph structures from graph theory.

The idea is that, we have a set of `n` nodes `V` (sometimes called vertices) and `m` edges `E`, which connect nodes to each other.

Graphs are denoted by `G = (V, E)`.

![undirected-graph](https://media.geeksforgeeks.org/wp-content/uploads/SIMPLE-GRAPH.jpg)
<em>Figure: An undirected graph with 5 nodes and 8 edges</em>

## Types of Graphs
A graph can either be **undirected**, meaning that the edges are "bidirectional" (e.g. can traverse from node `A` to node `B` and vice versa), or **directed**, meaning that its edges point to *specific* node(s), making it so that we can only travel from node `A` to node `B`, but not vice versa.

![graph-comp](https://www.differencebetween.com/wp-content/uploads/2011/05/DifferenceBetween_Directed_UnDirected_Graphs1.jpg)

Both of these graphs can have numerical weight values associated with each of its edges, which is called a **weighted graph**. An edge's weight value corresponds to some *cost measure* of traversing to and from the nodes that it connects.

![weighted-graph](https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/)

This is commonly used as a mathematical model for problems in computer science (or other engineering fields). Most notably, the [page ranking algorithm](https://en.wikipedia.org/wiki/PageRank) Google uses for its search engine results uses a directed weighted graph to determine which page should show up before others.

### Undirected graphs
Undirected graphs are pretty simple. It simply has `n` vertices and `m` edges, where the order of vertex pairs that form an edge don't matter. For example, if we have two vertices `v` and `u`, the edges `(v, u)` and `(u, v)` are equal.

#### Trees
An undirected graph can form a **tree**, which is basically an undirected graph where any two vertices `u` and `v` in `V` are connected by *exactly one* path.

![tree](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Tree_graph.svg/1200px-Tree_graph.svg.png)

Trees are especially useful for displaying information, like the shortest paths to all nodes in a directed graph from a source vertex `s` from Dijkstra's algorithm (using the parent array).

### Directed graphs
For directed graphs, the order of vertex pairs which form an edge *does* matter. Meaning, for two vertices `v` and `u`, `(v, u) != (u, v)`. However, some edges may be *bidirectional*, which basically means that the edge is undirected.

Because of this caveat, a lot of properties arise that distinguish different types of directed graphs from each other:
* Cyclic graphs
* Directed acyclic graph (DAG)

I'll briefly go over them below.

#### Cyclic graphs
A cyclic graph is a graph that contains a **graph cycle**, which is defined as the subset of vertices such that the last node in the subset can always be reached from the first.

![cyclic-graph](https://weirdo.dev/images/cyclic_graphs.png)

Notice how, in the graph above, node `B` reaches node `C`, node `C` reaches `E`, node `E` reaches `D`, and `D` reaches `B`, the first node in our path, thus making a cycle. If we looked at this cycle in terms of vertex pairs that form edges, we get `(B, C)`, `(C, E)`, `(E, D)`, and `(D, B)`. In other words, a cycle contains a path from at least one node back to itself.

Although this technically only applies to directed graphs, undirected graphs can be cyclic too. Can you guess why?

If you guessed that it's because undirected graphs can also be bidirectional, then you're right. There's an algorithm for detecting cycles in an undirected graph, called **Depth First Search** (DFS). Below is an undirected graph with a cycle:

![undirected-cyclic](https://media.geeksforgeeks.org/wp-content/uploads/20200508214739/Untitled-Diagram14115.png)

There's a cool property that comes with cyclic graphs, called **strongly connected components** (SCC). I'll explain in the subsection below.

#### Strongly connected components
A graph is **strongly connected** if every vertex `v` in the set of vertices `V` is reachable from every other vertex `u` in `V`.

![scg](https://www.cdn.geeksforgeeks.org/wp-content/uploads/connectivity3.png)

The set of vertices in a subgraph that is strongly connected is what we call a **strongly connected component**. 

To visualize, here's a graph with its strongly connected components marked.

![scc](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Scc.png/440px-Scc.png)

To further contextualize on this, let's use our previous cyclic graph example with the strongly connected components circled in red:

![cyclic-graph](https://i.imgur.com/i9BetYs.png?1)

As we can see, all the vertices in the cycle are reachable from one another. If we wanted to reach the vertex `F` from some node, we can do so by starting at any vertex `B`, `C`, `E`, or `D`. Therefore, it's safe to generalize these vertices into one "compressed" node (which is a strongly connected component):

![scc-one-node](https://i.imgur.com/4mLye1J.jpg)

If you want to see the usefulness in using strongly connected components, check out [this](https://www.youtube.com/watch?v=qz9tKlF431k) Google mock interview video.

### Directed acyclic graph (DAG)
A directed acyclic graph, often abbreviated to DAG, is a directed graph that contains no cycles. To visualize:

![dag](https://miro.medium.com/max/4000/1*Fi1AZPZLrGf-6wM_wTSPQw.png)

In my opinion, DAGs are probably the most useful type of graphs in terms of representing information. It's used in *machine learning* (unrolling recurrent neural networks for backpropogation, standard feedforward networks), *Bayesian statistics* (modelling probabilistic models like Bayesian networks), and *biogenetics* (family trees). 

Another cool thing about DAGs is that, we can make any directed graph a DAG if we compress its [strongly connected components](#strongly-connected-components).

## Adjacency Matrix
A graph with `n` nodes and `m` edges can be represented as an *n x n* matrix, where each entry indicates whether or not a vertex `v` and `u` are adjacent (forming an edge).

The figure below displays an undirected graph and its corresponding adjacency matrix.

![adj-mat](https://i.imgur.com/KyifR9h.png)


