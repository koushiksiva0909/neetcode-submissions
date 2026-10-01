class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num=[]
        for i in nums:
            if i!=0:
                num.append(i)
        for i in nums:
            if i==0:
                num.append(i)
        nums[:]=num
        