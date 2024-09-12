# https://leetcode.com/problems/concatenation-of-array/

'''
Problem: Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Solution: We can solve the problem by iterating through the array twice. We can append the elements of the array to the answer array twice.
'''  
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range (2): 
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans 

