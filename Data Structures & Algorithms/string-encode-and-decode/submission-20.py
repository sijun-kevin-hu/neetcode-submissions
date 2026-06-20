class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            l = len(st)
            res += str(l) + '#' + st
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        length = ""
        while i < len(s):
            if s[i] == '#':
                l = int(length)
                i += 1
                j = i + l
                string = s[i : j]
                i = j
                res.append(string)
                length = ""
            else:
                length += s[i]
                i += 1
        return res