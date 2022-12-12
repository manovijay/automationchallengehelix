n = 10
reverse = True
start = 0
end = n
step = 1
while(reverse):
    for i in range(start, end , step):
        for j in range(i, n):
            if (i == 0 or i == n-1 or j == i or j == n-1):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()
    if (step == -1):
        reverse = False
    start = n-1
    end = -1
    step = -1
