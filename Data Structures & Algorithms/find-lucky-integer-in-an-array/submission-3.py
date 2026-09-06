class Solution:
    def findLucky(self, arr: List[int]) -> int:

        arr_set = set(arr)
        ans = []
        
        for i in arr_set:
            if i == arr.count(i):
                ans.append(i)
        

        if len(ans) > 0 :
            return max(ans)
        else:
            return -1 


        