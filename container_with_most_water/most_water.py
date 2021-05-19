class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height)-1
        res = 0
        # if left_pointer = right_pointer, the base will be 0
        while left_pointer < right_pointer:
            # do not need to +1 since we are index by 0
            base = right_pointer - left_pointer
            y_axis = min(height[left_pointer], height[right_pointer])
            # if the left_pointer is the smaller one, increment it
            # if the right pointer is the smaller one, decrement it
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
            res = max(res, base * y_axis)
        return res
