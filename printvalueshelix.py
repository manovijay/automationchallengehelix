mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

n = 4
start, end = 0, n
inc = 1
k = n - 1
l = 0
rev = True

while rev:
    for i in range(start, end, inc):
        for j in range(i, end, inc):
            if l < n:
                if ((i == start and j < n - 1)
                        or (j == i + k and j == end - 1)
                        or (j == 0 and j == k + start)
                        or (j == 0 and j == k + i)
                        or (j == i - 1) and (j == start - 1)
                        or (j == end - 1) and (j == inc + 1)
                        or (j == start - 2 and j == inc + 1)):
                    print(mat[i][j], end=" ")
            elif l == n:
                if i > j and j == start - 1:
                    print(mat[i][j], end=" ")
        k = k - 1
    l = l + 1
    if l > n:
        rev = False
    if start == n - 1 and end == -1:
        end = n + end
        start = 1
        inc = 1
        n = n - 1
    elif start >= 0:
        start = n - 1
        end = -1
        inc = -1
