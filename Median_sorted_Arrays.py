class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lnums1 = len(nums1)
        lnums2 = len(nums2)
        flag = 1
        if (lnums1 + lnums2) % 2 == 0:
            index = (lnums1 + lnums2) / 2
            flag = 0
        else:
            index = (lnums1 + lnums2) / 2
            index += 1
            
        curr = 0
        curr_val = 0
        while curr != index:
            if nums1 == []:
                curr_val = nums2.pop(0)
                curr += 1
            elif nums2 == []:
                curr_val = nums1.pop(0)
                curr += 1
            else:
                if nums1[0] <= nums2[0]:
                    curr_val = nums1.pop(0)
                else:
                    curr_val = nums2.pop(0)
                curr += 1
        
        if flag == 0:
            if nums1 == []:
                sol = curr_val + nums2[0]
            elif nums2 == []:
                sol = curr_val + nums1[0]
            else:
                if nums1[0] <= nums2[0]:
                    sol = curr_val + nums1[0]
                else:
                    sol = curr_val + nums2[0]
            sol = sol / 2.0
        else:
            sol = curr_val
        print "Index", sol, index
        return sol
        