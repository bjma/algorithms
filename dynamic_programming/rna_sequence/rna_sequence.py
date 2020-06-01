# top-down recursive algorithm
def OPT(i, j, B):
    if i >= j - 4:
        return 0
    else:
        # check if i and j are paired
        # if not paired, then we get OPT(i, j - 1)
        unpaired = OPT(i, j - 1, B)
        
        # check if j is paired with some t 
        # where i <= t < j - 4
        pairing = [
            1 + OPT(i, t - 1, B) + OPT(t + 1, j - 1, B)
            for t in range (i, j - 4)
            # some unwritten code
            if is_pair(B[t], B[j]) 
        ]

        # if no pairs were found
        if not pairing:
            # reset
            pairing = [0]
        # else, get the max pairings from the bounds
        paired = max(pairing)

        return max(unpaired, paired)
