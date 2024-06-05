# https://leetcode.com/problems/remove-element/

'''
Problem: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Solution: We can solve the problem by using two pointers. We can iterate through the array with the right pointer.
If the element at the right pointer is equal to val, we set the element at the right pointer to 0. Otherwise, we copy the element at the right pointer to the left pointer and increment the left pointer.
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range (len(nums)):
            if nums[r] == val:
                nums[r] = 0
            else:
                nums[l] = nums [r]
                l+=1
        return l

