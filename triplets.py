def summer(a,b):
    z = len(a)
    y = len(b)
    result1 = []
    result2 = []
    for i in range(0, z ):
        for j in range(0, y):
            if i == j:
                if a[i] > b[j]:
                    result1. append(1)
                elif a[i] < b[j]:
                    result2.append(1)
                else:
                    pass
    return len(result1),len(result2)
    

        
a = [2,4,5,6]
b = [3,6,3,6]
print(summer(a,b))
