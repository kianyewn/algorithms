class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            median_num1 = total_length//2
            median_num2 = median_num1 + 1
            current_num = 0
            i, j = 0, 0
            m1, m2 = -1, -1
            # add sentinel
            nums1.append(10000000)
            nums2.append(10000000)
            # Bad thing about this is that we always need to handle the case where one of the index exceeds its length, and the other index has not exceed its length!
            # We solve this using the sentinel, so that the while loop will always run.
            # The sentinel will only be "added" after the original elements in either of the arrays are added
            # Another thing that needs to be handled is what if either of the array is empty...
            while i < len(nums1) and j < len(nums2):
                if nums1[i] >= nums2[j]:
                    if m1 is -1:
                        m1 = nums2[j]
                    elif m2 is -1:
                        m2 = nums2[j]
                    else:
                        m1 = m2
                        m2 = nums2[j]
                    j += 1
                else:
                    if m1 is -1:
                        m1 = nums1[i]
                    elif m2 is -1:
                        m2 = nums1[i]
                    else:
                        m1 = m2
                        m2 = nums1[i]
                    i += 1
                if i+j == median_num2:
                    m1s = "m1:" + str(m1)
                    m2s = "m2:" + str(m2)
                    print(m1s, m2s)
                    return float(m1+m2)/2
            return -1
        else:
            median_num = total_length//2 + 1
            i, j = 0,
            # this code originally failed at [],[1]. The issue is that the index exceeded the length of the array
            # Similarly, add an sentinel to make it complete.
            # i+j will always be == median_num at some point.
            nums1.append(100000)
            nums2.append(100000)
            current = None
            while i < len(nums1) and j < len(nums2):
                if i+j == median_num:
                    return current
                if nums1[i] >= nums2[j]:
                    current = nums2[j]
                    j += 1
                else:
                    current = nums1[i]
                    i += 1

            return current


def findMedianSortedArrays(nums1, nums2):
    # use the smaller of the array as the initialization for the binary search
    # Using the smaller array have the benefit that we will have fewer values to examine: https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
    m = len(nums1)
    n = len(nums2)
    # If m and larger than n, then we swap the references of the variables
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    # search on the smaller array
    iMin = 0
    iMax = m
    # By using this formula, the median will be contained in half_length if the sum of the length of the two arrays is odd.
    half_length = (m + n + 1) // 2
    # take note that iMin can be equals to iMax. This is when ALL of the elements in nums1 is in the "left" partition!!
    while iMin <= iMax:
        i = (iMin + iMax) // 2
        # if we did not the smaller array, there can be an issue in that (half_length - i) will be negative
        # half_length = (m+n+1)//2, if i is the index for the smaller array:
        # It is guaranteed that half_length will be greater than or equals to ANY index i
        # min(half_length) and suppose m == n, => ((m+m+1)//2 ~ m++ ) >= i
        j = half_length - i
        # print(i)
        # if i is too much such that there exist another value(that is the direct ancestor of a previous number) in nums2 that should be the median
        if i > 0 and nums1[i - 1] > nums2[j]:
            # print(f"cp:{1}")
            iMax = i - 1
        # if j is too much, it also implies that i is too small
        elif i < m and nums2[j - 1] > nums1[i]:
            # print(f"cp:{2}")
            # icreasing i is the same as decreasing j
            iMin = i + 1
            # print(iMin)
        else:
            # if our 'i' is perfect
            # Get the largest value that lie in the "left" partition
            if i == 0:
                # CORRECT if i == 0, this means that the entire "left" parition is from nums2.
                # WRONG if i == 0, this means that the entire  nums2 is inside the "left" parition.
                # The above statement is wrong because j = half_length - i and not j = n, so the entire nums2 will not be in the "left" partition.
                maxLeftNum = nums2[j - 1]
            # elif i == m: ## ** Important!: this statement should be checking for j == 0 (because we want to find the maximum value in the left partition)
                # WRONG: if i ==m, this means that the entire "left" parition is from nums1.
                # CORRECT: if i ==m, this means that the entire nums1 is inside the "left" parition.
                # THe abv statement is correct because we chose to search through the smaller array with index i, and when i == m, this means that the entire nums1 array is in the "left" partition.
                # if j == 0, this means that the entire "left" partition is from nums1.
                # WHY IS THIS WRONG: we know that the entire nums1 array is in the "left" partition, but the "left" partition MAY or MAY NOT contain number from the nums2.
                # Thus this statement cannot be used to check the maxLeftNum!
                # maxleftNum = nums1[i - 1]
            elif j == 0:
                # ** This means that the entire left partition is from nums1, and therefore we can choose nums1[i-1]!!
                maxLeftNum = nums1[i-1]
            else:
                # if i != 0 or i != m, then this means that the "left" partition contains a mix of numbers from nums1 and nums2
                # i-1 and j-1 correponds to the largest values respectively that are contained in the "left" parition since each array is sorted.
                maxLeftNum = max(nums1[i-1], nums2[j-1])
            # if the sum of the length of the two array is odd, then the median is just the max of the "left" parition
            if ((m + n) % 2) == 1:
                return maxLeftNum
            else:
                # print('hi')
                if i == m:
                    # if i == m, this means that the entire nums1 is in the "left" partition.
                    # Since we know that all the elements in nums1 is inside the "left" partition, minimum RHS value MUST BE in nums2
                    minRightNum = nums2[j]
                elif j == n:
                    # if  j ==n, this means that the entire nums2 is in the RHS partition, so minimum RHS value MUST BE in nums1
                    minRightNum = nums1[i]
                else:
                    minRightNum = min(nums1[i], nums2[j])
                return (maxLeftNum + minRightNum) // 2


arr1 = [1, 2, 3]
arr2 = [4, 5, 6, 7, 8]
res = findMedianSortedArrays(arr1, arr2)
print(res)
