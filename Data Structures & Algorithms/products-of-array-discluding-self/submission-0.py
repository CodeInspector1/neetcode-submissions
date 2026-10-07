class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        matrix = [1] * length

        first = 1
        second = 1

        for i in range(length):

            matrix[i] *= first
            first *= nums[i]
            
            j = length - 1 - i
            matrix[j] *= second
            second *= nums[j]
        
        return matrix
