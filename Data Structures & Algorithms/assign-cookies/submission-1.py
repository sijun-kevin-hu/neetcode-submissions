class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = sorted(g)
        cookies = sorted(s)
        content = 0

        i, j = 0, 0
        while i < len(children) and j < len(cookies):
            if children[i] <= cookies[j]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1
        return content
