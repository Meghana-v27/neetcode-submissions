class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for x in range(len(nums)):
            a=target-nums[x]
            if a in seen:
                return [seen[a],x]
            else:seen[nums[x]]=x