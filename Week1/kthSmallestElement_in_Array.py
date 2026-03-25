class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(Solution().kthSmallest(arr,k))