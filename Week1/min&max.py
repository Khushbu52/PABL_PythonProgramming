class Solution:
    def getMinMax(self, arr):
        arr.sort()
        min = arr[0]
        max = arr[len(arr)-1]
        return min, max
arr = [1,4,3,5,8,6]
print(Solution().getMinMax(arr))