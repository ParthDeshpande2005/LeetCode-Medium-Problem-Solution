class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        apple=0
        cnt=0
        while(apple<neededApples):
            cnt=cnt+1
            apple=apple+(12*cnt*cnt)
        return 8*cnt