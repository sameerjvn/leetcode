# leetcode 167 
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution():
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # time complexity: O[n]
        # space complexity: O[1]
        left, right = 0, len(numbers) - 1

        while left < right:

            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1                
            else:
                return [left + 1, right + 1]

        return []