class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        ans = arr[n-1] - arr[0]
        for i in range(1,n):
            if arr[i] - k < 0:
                continue
            mini = min(arr[0]+k, arr[i]-k)
            maxi = max(arr[i-1]+k, arr[n-1]-k)
            
            ans = min(ans, maxi-mini)
        return ans
arr = [1,5,8,10]
k = 2
print(Solution().getMinDiff(arr,k))