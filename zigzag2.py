def zizag(a, n):
    x = sorted(a)
    left = []
    right = []
    
    
    for i in range(0, n//2):
        left.append(x[i])
    for j in range(n//2 , n):
        right.append(x[j])
    x = left+sorted(right, reverse=True)
    w = len(x)
    for z in range(w):
        print(x[z], end = " ")


a = [1, 2, 3, 4, 7, 6, 5]
n = len(a)
(zizag(a, n))