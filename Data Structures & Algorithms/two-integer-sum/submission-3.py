class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        last = len(nums) - 1 
        print(last)

        while first < last:
            if nums[first] + nums[last] == target:
                return [first, last]

            last -= 1
            
            if first == last:
                first += 1
                last = len(nums) - 1