def plusMinus(arr):
    positive = []
    zero = []
    negative = []
    x = len(arr)
    for i in range(0, x):
        if arr[i] > 0:
            positive.append(arr[i])
        elif arr[i] == 0:
            zero.append(arr[i])
        else:
            negative.append(arr[i])

    
    formatted_positive = "{:.6f}".format((len(positive)/x))
    formatted_negative = "{:.6f}".format((len(negative)/x))
    formatted_zero = "{:.6f}".format((len(zero)/x))
    print(formatted_positive) 
    print(formatted_negative) 
    print(formatted_zero) 
    
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)