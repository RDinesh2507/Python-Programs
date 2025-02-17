class Solution(object):
    def uniqueOccurrences(self, arr):
        cnt = Counter(arr)
        return len(set(cnt.values())) == len(cnt)