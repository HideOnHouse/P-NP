class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        rtype: int
        """
        answer = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            temp = (right - left) * min(height[left], height[right])
            answer = max(temp, answer)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer
