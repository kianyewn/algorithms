class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the intervals according to the first value
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        res = []
        # current_candidate contains at most 2 intervals
        current_candidate = intervals[0]
        for interval in intervals[1:]:
            # if the current start is less than the previous end
            if interval[0] <= end:
                # merge while keeping the start intact since we sorted it already
                new_end = max(interval[1], end)
                current_candidate = [start, new_end]
                end = new_end
            elif interval[0] > end:
                res.append(current_candidate)
                current_candidate = interval
                start = interval[0]
                end = interval[1]
        res.append(current_candidate)
        return res
