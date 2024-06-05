# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

'''

Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

Solution: We can solve the problem by using two pointers. We can iterate through the array with the right pointer.
If the element at the right pointer is different from the element at the left pointer, we copy the element at the right pointer to the left pointer and increment the left pointer.

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1 

        for r in range(1, len(nums)):
            if nums[r] != nums [r-1]:
                nums[l] = nums [r]
                l+=1
        return l
