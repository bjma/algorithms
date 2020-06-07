# Merges two arrays
def merge(A, l, m, u):
    # initialize two subarrays and copy data
    L = [A[x] for x in range(m - l + 1)]
    R = [A[x] for x in range(u - m)]

    # index for L and R
    i = j = 0

    # index for merged subarray
    k = 1
    # merge by sorting then copying L and R elements into A
    while (i < len(L) and j < len(R)):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    # copy remaining elements of L and R into A
    while (i < len(L)):
        A[k] = L[i]
        i += 1
        k += 1

    while (j < len(R)):
        A[k] = R[j]
        j += 1
        k += 1

# Partitions A into subarrays
def sort(A, l, u):
    # still within bounds
     if (l < u):
        # get middle index
        m = (l + u) / 2

        # divide array into halves
        sort(A, l, m)
        sort(A, m + 1, u)

        # merge them
        merge(A, l, m, u)

if __name__ == '__main__':
    A = [38, 27, 43, 3, 9, 82, 10]
    sort(A, 0, len(A) - 1)
    print(A)