class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        res=[]
        for x in s:
            if x not in res:
                res.append(x)
                if(len(res)>max):
                    max = len(res)
            else:
                idx = res.index(x)
                res=res[(idx+1):]
                res.append(x)
        return max
