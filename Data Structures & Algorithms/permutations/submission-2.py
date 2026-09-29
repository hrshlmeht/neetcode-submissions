class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.curr = []
        def backtrack(remaining_nums):
            if len(self.curr) == len(nums):
                self.answer.append(self.curr.copy())
                # print("A",self.answer)
                return
            for i in range(len(remaining_nums)):
                # if i > len(remaining_nums): break
                # print(i,remaining_nums)
                chosen = remaining_nums.pop(i)
                self.curr.append(chosen)
                backtrack(remaining_nums.copy())
                self.curr.pop()
                remaining_nums.insert(i, chosen)
        backtrack(nums.copy())
        return self.answer