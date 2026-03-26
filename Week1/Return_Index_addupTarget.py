class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i,len(nums)-1):
                sum = nums[i]+nums[j+1]
                if(sum == target):
                    return (i,j+1)

arr = [2,7,11,15]
tar = int(input("Enter your target value: "))
print(Solution().twoSum(arr,tar))        