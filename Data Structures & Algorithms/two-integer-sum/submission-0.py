class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        extmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in extmap:
                return [extmap[diff],i]
            extmap[n]=i
            