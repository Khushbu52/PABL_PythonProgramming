class Solution:
    def largest(self, arr):
        max = arr[0]
        for num in arr[1:]:
            if num > max:
               max = num
        return max
        
arr = [1,8,7,56,90]
print(Solution().largest(arr))