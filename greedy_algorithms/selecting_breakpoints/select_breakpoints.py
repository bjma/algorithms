# Return breakpoint p s.t. b[p] <= x + C
# We can use binary search since b is sorted
def find_breakpoint(C, x, b):
    n = len(b)

    # distance until depletion
    dist = x + C

    # get middle index
    p = n // 2

    # split halves to look for max index
    left = find_breakpoint(C, x, b[:p - 1])
    right = find_breakpoint(C, x, b[:p + 1])

    # find breakpoint
    if b[p] < b[left] and b[left] <= dist:
        p = left
    if b[p] < b[right] and b[right] <= dist:
        p = right
    return p

# Also called truck driver's algorithm
# Let b be the set of breakpoints
# Let C be the fuel capacity
def select_breakpoints(C, b):
    # total distance
    n = len(b)

    # sort breakpoints in increasing order
    b.sort()

    # total distance
    L = b[n]

    # init solution set S for appending breakpoints
    S = []

    # init curr. distance x
    x = 0

    # begin our trip
    while (x < L):
        # find breakpoint p s.t. b[p] <= x + C
        p = find_breakpoint(C, x, b)
        # no solution
        if (b[p] == x):
            return [0]
        x = b[p]
        S.append(p)
    return S

if __name__ == '__main__':
    b = [0, 1, 4, 6, 2, 8, 3, 10, 17, 23, 30, 31, 24, 35]
    C = 7
    S = select_breakpoints(C, b)
    print(S)
    