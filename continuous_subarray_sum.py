from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        maxd, mind = deque(), deque()   # deques for max and min
        i = res = 0

        for j, num in enumerate(nums):
            # Maintain decreasing deque for max
            while maxd and num > maxd[-1]:
                maxd.pop()
            maxd.append(num)

            # Maintain increasing deque for min
            while mind and num < mind[-1]:
                mind.pop()
            mind.append(num)

            # If window invalid, shrink from left
            while maxd[0] - mind[0] > limit:
                if nums[i] == maxd[0]:
                    maxd.popleft()
                if nums[i] == mind[0]:
                    mind.popleft()
                i += 1

            # Update max length
            res = max(res, j - i + 1)

        return res