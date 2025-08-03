class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        snew="" 
        if(numRows==1):
            return s
        if(numRows>1):
            for i in range(numRows):
                for y in range(len(s)):
                    if(y%(numRows+(numRows-2))==i or y%(numRows+(numRows-2))==(numRows+(numRows-2)-i)):
                        snew=snew+s[y]
            return snew 