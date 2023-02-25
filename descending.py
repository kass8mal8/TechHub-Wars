""" Function taking non-negative number and return digits in descendong order """


def descending(num):
    rem, num_rem = num % 10, abs(num)
    arr = []

    while num_rem:
        rem, num_rem = num_rem % 10, num_rem // 10
        arr.append(rem)
    arr.sort(reverse=True)
    print(arr)


descending(162)
