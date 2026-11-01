class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(indice=0,curr=[]):
            if indice >= len(nums) :
                res.append(curr)
                return
            dfs(len(nums),curr)
            for i in range(len(nums[indice:])):
                if  i==0 or (i!=0 and nums[indice+i-1]!=nums[indice+i]) :
                    dfs(indice+1+i,curr+[nums[i+indice]])

        dfs()
        return res