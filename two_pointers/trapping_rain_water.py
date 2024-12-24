# leetcode 42
# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: list[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL <= maxR:
                l += 1 # why do we shift before calculating the max?
                maxL = max(maxL, height[l]) # why do we include the current position in the max computation?
                level = maxL - height[l]
                if level < 0:
                    level = 0
                res += level
            else:
                r -= 1
                maxR = max(maxR, height[r])
                level = maxR - height[r]
                if level < 0:
                    level = 0
                res += level
            
        return res

