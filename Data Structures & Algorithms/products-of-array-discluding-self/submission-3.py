class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count >= 2:
                    return [0] * len(nums)
            else:
                product *= num
        
        output = [0] * len(nums)
        for i, num in enumerate(nums):
            if num != 0 and zero_count == 1:
                continue
            elif num == 0:
                output[i] = product
            else:
                output[i] = product // num
        return output



        