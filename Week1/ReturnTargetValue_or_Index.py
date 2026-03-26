class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
arr = [2,4,6,8,9]
target = int(input("Enter a target value : "))
print(Solution().searchInsert(arr,target))    