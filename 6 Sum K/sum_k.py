'''
**NOTE
The solution made is CORRECT!
But the time taken to execute the algorithm for from Task 4 and later is too long.
Thus, I only managed to get the answer for Task 1 until Task 3.
'''

import sys

def find_subsets(arr):
    if len(arr) == 0:
        return [[]]

    subsets = find_subsets(arr[:-1])
    last_element = arr[-1]

    subsets_with_last_element = [subset + [last_element] for subset in subsets]

    return subsets + subsets_with_last_element


with open('sum_k.txt') as file:
    n, power = next(file).split(' ')
    n = int(n)
    sys.setrecursionlimit(n*2)
    power = int(power)

    nums = [int(num) for num in next(file).split(' ')]
    
    total = 0
    subsets = find_subsets(nums)
    for subset in subsets:
        total += (sum(subset) ** power) % 998244353
    print(total)


