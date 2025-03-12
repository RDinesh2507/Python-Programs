class Solution(object):
    def lengthOfLastWord(self, s):
        if not s or not s.split():
            return 0
        return len(s.split()[-1])
    def lengthOfLastWord2(self,s):
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
if __name__ == '__main__':
    sol = Solution()
    s = "hello world"
    print sol.lengthOfLastWord(s)
    s = "hello"
    print sol.lengthOfLastWord(s)
    print sol.lengthOfLastWord2(s)
    s = " "
    print sol.lengthOfLastWord(s)
    print sol.lengthOfLastWord2(s)
 
 