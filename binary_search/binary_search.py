class Solution(object):

    def wrong_search(self, nums, target):
        # this search is wrong because when we do self.search(nums[:mid], target),
        # our indexes will be based on this sublist.
        # for example, nums = [0,1,2,3] nums[2:] = [2,3], the element 2 is located at index 2 in nums, while element 2 is located at index 0 in nums[2:]. This lead to the discrepancy in the results.
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    return self.search(nums[:mid], target)
                elif nums[mid] < target:
                    return self.search(nums[mid+1:], target)

        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
