# Container with most water
class Solution(object):
    def maxArea(self, height):
        l = len(height) - 1
        start = 0
        volume = 0
        while start < l:
            if height[start] > height[l]:
                temp = (l - start) * height[l]
                if temp > volume:
                    volume = temp
                l -= 1
            else:
                temp = (l - start) * height[start]
                if temp > volume:
                    volume = temp
                start += 1
        print volume
        return volume