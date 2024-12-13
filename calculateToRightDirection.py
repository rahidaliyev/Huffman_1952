def CalculateRightDirection(arr=[]):
    while len(arr)>1:
        a = arr.pop() + arr.pop(-1)
        arr = arr[:-2]
        arr.append(a)
        arr.sort(reverse=True)
        print(arr)
    