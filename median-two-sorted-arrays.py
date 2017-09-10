import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=sorted(nums1+nums2)
        if(len(nums3)%2!=0):
            return nums3[(len(nums3))/2]
            
        else:
            idx = len(nums3)/2
            res =(nums3[idx]+nums3[idx-1])/2.0
            return res
