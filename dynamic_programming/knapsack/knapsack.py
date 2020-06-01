# bottom-up knapsack
# parameters: 
# C -> max capacity
# items -> list of tuples, 1st entry is val, 2nd entry is weight
# n -> num items
def knapsack(C, items, n):
    # init memoization table
    V = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        # loop through weights
        for w in range(C + 1):
            w_i = items[i - 1][1]
            v_i = items[i - 1][1]
            if i == 0 or w == 0:
                V[i][w] = 0
            elif items[i - 1][1] <= w:
                V[i][w] = max(V[i - 1][w], v_i + V[i - 1][w - w_i])
            else:
                V[i][w] = V[i - 1][w]
    return V[n][C]
