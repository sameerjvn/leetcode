# leetcode 15
# https://leetcode.com/problems/3sum/

class Solution():
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums: [1, -1, 0, 1, 2, -2]
        # sorted nums: [-2, -1, 0, 1, 1, 2]
        # soln: [
        #   [-2, 0, 2]
        #   [-2, 1, 1]
        #   [-1, 0, 1]
        # ]
        # nums: [-1, -1, 0, 1, 2, -2]
        # sorted nums: [-2, -1, -1, 0, 1, 2]
        # soln: [
        #   [-2, 0, 2]
        #   [-1, 0, 1]
        #   [-1, -1, 2]
        # ]
        # time complexity : O(n log(n)) from sorting + O(n^2) = O(n^2)
        # space complexity : O(1) or O(n) for depending on sorting algorithm

        results = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue

            l, r = i+1, len(nums) - 1

            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    results.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return results