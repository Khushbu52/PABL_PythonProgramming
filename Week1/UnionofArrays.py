class Solution:    
    def findUnion(self, a, b):
        return sorted(set(a) | set(b))
a = [1,2,3,4,5]
b = [1,2,3]
print(Solution().findUnion(a,b))