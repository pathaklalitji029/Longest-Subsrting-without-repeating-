class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        #here we check the base case if length of string is zero then return 0
        if n==0:
            return 0
        ans=1
        #makeing the empty hashset
        set1=set({})

        #here we insert the first letter of string to the set 
        set1.add(s[0])

        #now takig the two loops to traverse the loop till end of string
        i=0
        j=1

        while j < n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            ans=max(ans,(j-i))
        return ans

s="abcabcbb"


result=Solution()
print(f"The answer is {result.lengthOfLongestSubstring(s)}")



        


        
        
