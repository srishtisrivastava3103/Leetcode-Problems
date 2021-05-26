# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = 0
        prev = 0
        m = len(nums1)
        n = len(nums2)
        median = (n+m)//2
        i = j = 0
        while median>=0:
            prev = mid
            if i<m and j<n and nums1[i]<=nums2[j]:
                mid = nums1[i]
                i+=1
            elif i<m and j<n and nums1[i]>nums2[j]:
                mid = nums2[j]
                j+=1
            elif i<m:
                mid = nums1[i]
                i+=1
            elif j<n:
                mid = nums2[j]
                j+=1
            median-=1
        if (m+n)%2==0:
            return (prev+mid)/2
        return mid
            

            