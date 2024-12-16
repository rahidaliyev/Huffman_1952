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
