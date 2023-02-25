""" Algorithm to return sum of multiples of 3 and 5  """
# Time Complexity is O(n)


def multiple_sum(num):
    arr = []
    for n in range(1, num):
        if (n % 3 and n % 5) == 0:
            arr.append(n)
        else:
            if (n % 3 or n % 5) == 0:
                arr.append(n)

    return sum(arr)


print(multiple_sum(15))
