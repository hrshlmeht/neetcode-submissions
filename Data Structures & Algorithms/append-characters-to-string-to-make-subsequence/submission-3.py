# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:

#         if t in s:
#             return 0
        
#         s_array = []
#         t_array = []

#         for i in s:
#             s_array.append(i)
        
#         for j in t:
#             t_array.append(j)
        

#         count = 0

#         for i in s_array:
#             if i in t_array:
#                 continue
#             else:
#                 count +=1
        

#         return count

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        j = 0

        for i in s:
            if j < len(t) and i == t[j]:
                j += 1

        return len(t) - j
    
        