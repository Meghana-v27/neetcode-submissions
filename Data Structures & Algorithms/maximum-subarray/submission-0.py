class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        sum=nums[0]
        for x in nums[1:]:
            if x>curr+x:
                curr=x
            else:
                curr=curr+x
            if curr>sum:
                sum=curr
        return sum
            