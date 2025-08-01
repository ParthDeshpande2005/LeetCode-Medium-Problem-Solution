s="asjrgapa"
nums=[]
temp=[]
cnt=0
if(s==""):
    print("0")
for i in range(len(s)):
    y=i
    temp=[]
    cnt=0
    while(y<len(s) and s[y] not in temp):
        temp.append(s[y])
        cnt=cnt+1
        if(y==len(s)-1):
            nums.append(cnt)
        y=y+1
    nums.append(cnt)
    # for y in range(i,len(s)):
    #     if s[y] in temp:
    #         nums.append(cnt)
    #         temp=[]
    #         if(y==len(s)-1):
    #             nums.append(cnt)
    #         break
    #     else:
    #         temp.append(s[y])
    #         cnt=cnt+1
    #         if(y==len(s)-1):
    #             nums.append(cnt)
                
nums.sort()
print(nums)



#leetcode 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        nums=[]
        temp=[]
        cnt=0
        if(s==""):
            return 0
        for i in range(len(s)):
            y=i
            temp=[]
            cnt=0
            while(y<len(s) and s[y] not in temp):
                temp.append(s[y])
                cnt=cnt+1
                if(y==len(s)-1):
                    nums.append(cnt)
                y=y+1
            nums.append(cnt)
            # for y in range(i,len(s)):
            #     if s[y] in temp:
            #         nums.append(cnt)
            #         temp=[]
            #         if(y==len(s)-1):
            #             nums.append(cnt)
            #         break
            #     else:
            #         temp.append(s[y])
            #         cnt=cnt+1
            #         if(y==len(s)-1):
            #             nums.append(cnt)

        nums.sort()
        return nums[-1]