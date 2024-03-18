class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons based on their end points
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for start, _end in points[1:]:
            if start > end:
                # Need to shoot a new arrow
                arrows += 1
                end = _end

        return arrows