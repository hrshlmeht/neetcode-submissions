class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0 
        for i in range(0,len(s)):
            if s[i] == ' ':
                count = 0
            else:
                count +=1 
        

        return count


            


        