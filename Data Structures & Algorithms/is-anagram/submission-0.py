class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        list_s = list(s)
        list_t = list(t)

        for element in list_s:
            dict_s[element] = dict_s.get(element, 0) + 1
        
        for element in list_t:
            dict_t[element] = dict_t.get(element, 0) + 1

        if dict_s == dict_t:
            return True

        return False         