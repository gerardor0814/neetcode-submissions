class Solution:

    def encode(self, strs: List[str]) -> str:
        retval = ""
        for s in strs:
            retval += s + "%" + str(len(s)) + "%"
        return retval

    def decode(self, s: str) -> List[str]:
        retval = []
        i = 0
        while i < len(s) - 1:
            if s[i] == '%' and s[i + 1].isdigit():
                offset = 0
                i += 1
                while s[i] != "%":
                    print(s[i])
                    i += 1
                    offset += 1
                length = int(s[i - offset : i])
                retval.append(s[i - offset - length - 1: i - offset - 1])
            i += 1
        return retval