class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        def get_slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0:
                return (0, p1[1])
            if dy == 0:
                return (p1[0], 0)
            d = gcd(dx, dy)
            return (dx//d, dy//d)

        ans = 0
        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(i + 1, len(points)):
                d[get_slope(points[i], points[j])] += 1
            for v in d.values():
                ans = max(ans, v)
        return ans + 1