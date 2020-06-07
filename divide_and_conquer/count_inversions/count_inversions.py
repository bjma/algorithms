def sort_and_count(A):
    if len(A) == 1:
        return 0
    else:
        # partition array
        left_bound = len(A) / 2
        right_bound = len(A) - left_bound
        L = [A[x] for x in range(left_bound)]
        R = [A[x] for x in range(right_bound)]

        # now sort and count both
        L_inv, L = sort_and_count(L)
        R_inv, R = sort_and_count(R)
        # then merge both subarrays
        inv = merge_and_count(L, R)
        # return number of inversions and new sorted array
        num_inversions = L_inv + R_inv + inv
        return num_inversions, A

def merge_and_count(L, R):
    n = len(L) - 1
    m = len(R) - 1
    # temp array for merging
    A = []
    i = j = 0
    count = 0
    while L and R:
        # append min value; we do this
        A.append(min(min(L), min(R)))
        # if there is an inversion at j,
        # then count for the rest starting at i
        if R[j] < L[i]:
            # we can also use n - (i + 1)
            count += [1 for x in range(i + 1, n)]
            # now look at next element in R
            # to find more inversions
            j += 1
        else:
            # else, no need to look so continue
            i += 1
    # if L is empty, append the rest of R into list
    # this is fine since it's sorted
    if not L:
        for x in range(j, m):
            A.append(R[x])
    # likewise if R is empty
    if not R:
         for x in range(i, n):
            A.append(L[x])
    # return count and sorted merged array
    return count, A

if __name__ == '__main__':
    A = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
    A = sort_and_count(A)
    print(A)