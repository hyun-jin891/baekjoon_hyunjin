def binary_search(a, x):
    left = 0
    right = len(a)
    
    while left < right:
        mid = (left + right) // 2
        if a[mid] > x:
            left = mid + 1
        elif a[mid] < x:
            right = mid
        else:
            return 1
    
    return 0

N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
M = int(input())
num_l = list(map(int, input().split()))

for i in num_l:
    print(binary_search(arr, i))