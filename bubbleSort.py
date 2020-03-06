import swapElements as se


def bubblesort(A):
    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                se.swap(A, j, j + 1)
                swapped = True
            yield A
