class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for n in nums:
            if n in d:
                d[n]+=1
            else:d[n]=1
        for x in d.values():
            if x>1:
                return True
        return False