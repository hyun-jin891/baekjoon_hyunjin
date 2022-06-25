def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2   
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
num_l = list(map(int, input().split()))

for i in num_l:
    print(binary_search(arr, i, 0, N-1))