class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        znew=""
        for i in range(len(s)):
            z=""
            for y in range(i,len(s)):
                z=z+s[y]
                if(z==z[::-1]):
                    if(len(znew)<len(z)):
                        znew=z
        return znew