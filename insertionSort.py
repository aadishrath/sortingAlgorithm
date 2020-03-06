import swapElements as se


# insertion sort algorithm
def insertionsort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            se.swap(A, j, j - 1)
            j -= 1
            yield A
