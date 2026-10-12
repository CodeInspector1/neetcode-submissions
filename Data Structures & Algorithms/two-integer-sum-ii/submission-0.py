class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_point = 0
        second_point = len(numbers) - 1

        while first_point < second_point:
            curr_sum = numbers[first_point] + numbers[second_point]

            if curr_sum == target:
                return [first_point + 1, second_point + 1]

            elif curr_sum > target:
                second_point -= 1
            
            else:
                first_point += 1
            
        return []
