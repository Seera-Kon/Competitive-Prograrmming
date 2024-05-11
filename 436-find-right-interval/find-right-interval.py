class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        sorted_intervals = sorted((start, end, idx) for idx, (start, end) in enumerate(intervals))
        
        result = [-1] * len(intervals)
        
        for start, end, idx in sorted_intervals:
            target = end
            right_idx = bisect.bisect_left(sorted_intervals, (target, float('-inf'), float('-inf')))
            if right_idx < len(intervals):
                result[idx] = sorted_intervals[right_idx][2]
        
        return result