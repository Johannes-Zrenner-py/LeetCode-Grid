# Problem: 1929. Concatenation of Array
# Link: https://leetcode.com/problems/concatenation-of-array/
# Schwierigkeit: Easy

class Solution(object):
    def getConcatenation(self, nums):
        nums.extend(nums)
        return nums
