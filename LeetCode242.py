""" 
Problem: https://leetcode.com/problems/valid-anagram/

Description: Given two strings s and t , write a function to determine if t is an anagram of s.

Explaination:  First, we can check if the lengths of the two strings are equal. 
If they are not equal, the second string cannot be an anagram of the first string.
We can use a hash map to store the frequency of each character in the first string. 
Then, we can compare the frequency of each character in the second string with the hash map. 
If the frequencies are the same, the second string is an anagram of the first string. Otherwise, it is not an anagram.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        setA = {}
        setB = {}

        for char in s:
            setA[char] = setA.get(char, 0) + 1
        
        for char in t:
            setB[char] = setB.get(char, 0) + 1

        return setA == setB