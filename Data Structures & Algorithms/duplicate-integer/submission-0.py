class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # new array, store unseen elements (for all elements in nums)
        # return true if it matches the value in that new array
        # return false
        new_num = []
        for num in nums:
            if num not in new_num:
                new_num += [num]
            else:
                return True
        return False
        