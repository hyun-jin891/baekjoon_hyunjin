def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            left = mid + 1
        elif arr[mid] < x:
            right = mid - 1
        else:
            return 1
    if left == right and arr[left] == x:
        return 1
    return 0

N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
M = int(input())
num_l = list(map(int, input().split()))

for i in num_l:
    print(binary_search(arr, i))