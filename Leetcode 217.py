# https://leetcode.com/problems/contains-duplicate/

'''
Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Solution: We can solve the problem by using a hashset. We can iterate through the array and check if the element is already in the hashset. 
If it is, we return True. If it is not, we add the element to the hashset. If we finish iterating through the array without finding any duplicates, we return False.

'''  
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset = set()

         for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
         return False