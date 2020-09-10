def insertion(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def rev_insertion(A):
    n = len(A)
    for j in range(n - 1, -1, -1):
        key = A[j]
        i = j + 1
        while i < n and A[i] > key:
            A[i - 1] = A[i]
            i += 1
        A[i - 1] = key


if __name__ == "__main__":
    A = [5, 2]
    insertion(A)
    print(A)
