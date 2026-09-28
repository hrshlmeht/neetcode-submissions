class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        candidates.sort()

        # i and total should be 0
        def dfs(i: int, total: int):

            # Valid subset
            if total == target:
                res.append(subset.copy())
                return
            
            elif total > target:
                return
            
            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                # now this is the first time we see canidates[j]
                subset.append(candidates[j])

                dfs(j + 1, total + candidates[j])

                subset.pop()

        dfs(0, 0)

        return res