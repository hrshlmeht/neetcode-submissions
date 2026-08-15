class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for i in range(len(s)):

            if s[i] in pairs:
                # closing bracket

                if not stack:
                    return False

                if stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False

            else:
                # opening bracket
                stack.append(s[i])

        return len(stack) == 0