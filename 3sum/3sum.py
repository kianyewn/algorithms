def threeSum(nums):
    res = []
    nums = sorted(nums)
    for i in range(len(nums)):
        # choose a non duplicated starting number
        # i == 0 is needed so that the first character will be chosen as the starting position
        if (nums[i] != nums[i-1] and i > 0) or (i == 0):
            fixedStart = nums[i]
            remaining_sum = 0 - fixedStart
            low = i + 1
            high = len(nums) - 1
            while low < high:
                # print([nums[i], nums[low], nums[high]])
                if (nums[low] + nums[high]) == remaining_sum:
                    # print(low, high)
                    res.append([nums[i], nums[low], nums[high]])
                    # since nums[low] is added, we want to add the next value that is NOT A duplicate
                    # 1. since we are decrementing high, we need to make sure that our high - 1 is always > 0
                    # 2. nums[high] == nums[high-1] is to check for duplicates. if nums[high] == nums[high-1] is the same, we should not include it
                    while (nums[low] == nums[low + 1]) and (low + 1 < len(nums)) and (low < high):
                        low += 1
                    # 1. since we are incrementing low, and that we want (low+1), we need to make sure that our (low+1) is < len(nums)
                    # 2. nums[low] == nums[low+1] is to check for duplicates. if nums[low] and nums[low+1] is the same, then we should not include it
                    while (nums[high] == nums[high - 1]) and (high - 1 >= 0) and (low < high):
                        high -= 1
                    # at this point, we know that nums[high - 1] is different from nums[high], and since we want nums[high-1],
                    high -= 1
                    # at this point, we know that nums[low + 1] is different from nums[low], and since we want nums[low+1],
                    low += 1
                # if the sum is too large, we decrement the high
                elif (nums[low] + nums[high]) > remaining_sum:
                    # 1. since we are decrementing high, we need to make sure that our high - 1 is always > 0
                    # 2. nums[high] == nums[high-1] is to check for duplicates. if nums[high] == nums[high-1] is the same, we should not include it
                    # 3 Although we are decrementing high, we also need to ensure that low < high, as if low == high, then it will just be the same element.
                    #   if low > high, then we are just repeating the elements, as the high would have "covered" them once already.
                    # NOTE: actually we do not need the line below because this condition is when the sum is not equals to the remaining sum,
                    #       So even if our nums[high] is duplicated, it will NOT affect our results either way
                    # while (high - 1 > 0) and (nums[high] == nums[high - 1]) and (low < high):

                    high -= 1
                # if the sum is too small, then we increment the low
                elif (nums[low] + nums[high]) < remaining_sum:
                    # 1. since we are incrementing low, and that we want (low+1), we need to make sure that our (low+1) is < len(nums)
                    # 2. nums[low] == nums[low+1] is to check for duplicates. if nums[low] and nums[low+1] is the same, then we should not include it
                    # 3. Although we are incrementing low, we also want to make sure that our low < high, as if low == high, then it will just be the same element, and thus not valid
                    # NOTE: actually we do not need the line below because this condition is when the sum is not equals to the remaining sum,
                    #       So even if our nums[low] is duplicated, it will NOT affect our results either way
                    # while (low+1 < len(nums)) and nums[low] == nums[low + 1] and (low < high):
                    low += 1
    return res


tc = [-1, 0, 1, -1, 2, -4]  # [-4,-1,-1,0,1,2]
print(threeSum(tc))
# if you got : [[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]], the reason is because you have a duplicated starting position. For example, your stat can be index 1 and 2,
# which are both -1 and -1, and will give back the same result.


# MY SOLUTION FROM LEETCODE
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        indices_set = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if (i != j) and (i != k) and (j != k)\
                            and ((nums[i]+nums[j]+nums[k]) == 0):
                        candidate = [nums[i], nums[j], nums[k]]
                        if (candidate not in res) and ({nums[i], nums[j], nums[k]} not in indices_set):
                            d = {i, j, k} not in indices_set
                            # print((i,j,k),d)
                            res.append(candidate)
                            indices_set.append({nums[i], nums[j], nums[k]})
        return

    def threeSum(self, nums):
        # sort the array so that we can find the result
        nums = sorted(nums)
        # print(sorted_nums)
        res = []
        for i in range(len(nums)-2):
            # if the current summand is not in the first position already
            if (i == 0) or ((nums[i] != nums[i-1]) and (i > 0)):
                fixed_start = nums[i]
                remaining_sum = 0 - nums[i]
                low = i + 1
                high = len(nums) - 1
                # remove equality because is low = high, then this is just the same number
                while low < high:
                    # mid = (low + high) // 2
                    # print(low, high)
                    two_sum = nums[low] + nums[high]
                    # print(i, nums[i], two_sum, remaining_sum)
                    if two_sum == remaining_sum:
                        res.append([nums[i], nums[low], nums[high]])
                        # need to increment the low and high in this if statement, if not will lead to massive recursion error
                        # once we found a candidate, decide on what is next to do.

                        # NOTE!!
                        # We are changing the values of high and low TOGETHER, and not one at a time,
                        # because changing the value of one of the summand will NEVER be 0, i.e if x + y + z = 0, x + (y+delta) + z != 0
                        # Make sure that our next low value is not a duplicate of the current low value
                        # If low and high is the same, then no point, it will just be a duplicate
                        # NOTE: Whenever we are trying to increment our low and high, remember to keep track of the condition
                        # that our low must be less than or equals to our high.
                        # print(low)
                        while (low+1 < len(nums)) and (nums[low] == nums[low+1]) and (low < high):
                            # if low == 3:
                            # print(nums[low], nums[low+1])
                            low = low + 1

                        # Similar to low, Make sure that our next high value is not a duplicate of the current high value
                        while (high-1 >= 0) and (nums[high] == nums[high-1]) and (low < high):
                            high = high - 1

                        # so at this point, we know that the next low of the current low is different
                        low += 1
                        # so at this point, we also know that the next high of the current high is different
                        high -= 1
                    # if too much, decrement "high" since our array is sorted
                    if two_sum > remaining_sum:
                        high = high-1
                    if two_sum < remaining_sum:
                        low = low + 1

        return res
