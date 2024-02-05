import timeit

def fib_dp(num):
    arr = [0, 1]
    print("Dynamic Programming Approach:", end=' ')

    if num == 1:
        print('0')
    elif num == 2:
        print('[0, 1]')
    else:
        start_time = timeit.timeit()  # Record the starting time

        while len(arr) < num:
            arr.append(0)

        if num == 0 or num == 1:
            return 1
        else:
            arr[0] = 0
            arr[1] = 1

            for i in range(2, num):
                arr[i] = arr[i-1] + arr[i-2]

            end_time = timeit.timeit()
            execution_time = end_time - start_time
            print(arr)
            print("Execution time:", execution_time, "seconds")

            return arr[num-2]

fib_dp(5)
