# Problem: 1480. Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Schwierigkeit: Easy

class Solution(object):
    def runningSum(self, nums):
        neue_liste = []
        for i in range(len(nums)):
            neue_liste.append(sum(nums[:i+1]))
        return neue_liste
