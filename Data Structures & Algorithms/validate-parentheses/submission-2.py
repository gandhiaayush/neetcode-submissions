import enum



class Solution:
    def isValid(self, s: str) -> bool:
        store = []




        for index in range(len(s)):
            if len(store) != 0 and s[store[-1]] + s[index] in ("{}","()","[]"):
                store.pop()
                continue
            store.append(index)
        if len(store) == 0:
            return True
        return False