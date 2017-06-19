# Merge 2 sorted Lists
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        length = m + n - 1
        index = m - 1
        jndex = n - 1
        while length < m + n and index >= 0 and jndex >= 0:
            if nums1[index] > nums2[jndex]:
                nums1[length] = nums1[index]
                index -= 1
            else:
                nums1[length] = nums2[jndex]
                jndex -= 1
            length -= 1
        
        while index >= 0:
            nums1[length] = nums1[index]
            index -= 1
            length -= 1
        
        while jndex >= 0:
            nums1[length] = nums2[jndex]
            jndex -= 1
            length -= 1
        
        