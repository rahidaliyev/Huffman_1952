def CalculateRightDirection(arr=[]):
    print(arr)
    while len(arr)>1:
        a = arr.pop() + arr.pop(-1)
        arr.append(a)
        arr.sort(reverse=True)
        print(arr)
    