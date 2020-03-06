# swaps elements i and j of the array A[]
def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]
