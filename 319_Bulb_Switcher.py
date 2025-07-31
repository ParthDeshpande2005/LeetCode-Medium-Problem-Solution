class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """cnt=0
        for i in range(n+1):
            num=0
            
            for z in range(1,i+1):
                if(i%z==0):
                    num=num+1
            if(num%2!=0):
                cnt=cnt+1   """     
        return int(n**0.5)