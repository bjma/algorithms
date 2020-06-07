# idk if this code runs correctly btw
def closest_pair(P):
    # len(P) = len(x) = len(y) im pretty sure
    n = len(P)
    # partition into two regions
    mid = n / 2
    L = P[:mid]
    R = [mid:]

    # get closest pairs
    line1 = closest_pair(L)
    line2 = closest_pair(R)
    # min pair between gradient 
    line_LR = min(line1, line2)
    # remove all points out of bounds line_LR
    P = [P[x] for x in range (n) if P[x] < line_LR]
    # sort y-coordinates
    P = sort_by_ycoord(P)
    # scan points across gradient in y-order
    line = closest_split_pair(P, mid, line_LR)
    # return shortest line
    return min(line, line_LR)

# finds closest pair across gradient
def closest_split_pair(P, L, pair):
    # init default pairing
    line = dist(P[0], P[mid])
    # search through each point
    for i in range(len(P)):
        # search through each point across gradient
        for j in range(L, len(P)):
            p, q = P[i], P[j]
            dst = dist(p, q)
            line = min(dst, line)
    return line



# compute euclidean distance
def dist(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# sort P by y-coordinates
def sort_by_ycoord(P):
    n = len(P)
    # simple bubble sort
    for i in range(n):
        for j in range(n):
            if P[i][1] > P[j][1]:
                P[i], P[j] = P[j], P[i]
    return P