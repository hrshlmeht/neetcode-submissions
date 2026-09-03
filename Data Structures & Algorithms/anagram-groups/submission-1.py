class Solution:
    #brute force approach by converting to set and seeing
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     s_ans = []
    #     ans = []
    #     for i in strs:
    #         s = set(i)
    #         s_ans.append(s)
        
    #     #print(len(s_ans))
    #     for j in range(0 , len(s_ans)):
    #         for k in range(0 , len(s_ans)):
    #             if s_ans[j] == s_ans[k]:
    #                 ans.append(s_ans[j])
    

    #     print(ans)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in ans:
                ans[key] = []

            ans[key].append(word)

        return list(ans.values())


