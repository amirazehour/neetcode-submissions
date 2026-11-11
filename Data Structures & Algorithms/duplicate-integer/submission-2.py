class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d ={value : index for index , value in enumerate(nums)}

        if len(d)<len(nums):
            return True
        else :
            return False

        