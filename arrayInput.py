def InputArray(arr,num,sum):
    for i in range(int(num)):
        while True:
            n = input("num: ")
            n = float(n)

            if round(sum + n,2) > 1:
                print("Array sum cannot be more than 1. Please enter a smaller number.")
            else:
                arr.append(n)
                sum = round(sum + n,2) 
                break

    return(arr)


def InputArrayPredefined(arr, num, sum):
    predefined_values = [0.2, 0.18, 0.1, 0.1, 0.1, 0.06, 0.06, 0.04, 0.04, 0.04, 0.04, 0.03, 0.01]
    for n in predefined_values:
        if round(sum + n, 2) > 1:
            print("Array sum cannot be more than 1. Please check the predefined values.")
            return arr
        else:
            arr.append(n)
            sum = round(sum + n, 2)
    return arr
