class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        return ''.join(c*v for c,v in sorted(c.items(),key=lambda x: -x[1]))