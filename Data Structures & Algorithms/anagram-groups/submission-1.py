class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        count = [0] * 26
        hashmap = {}
        output = []

        for index, word in enumerate(strs):
            count = [0] * 26
            word = list(word)
            for char in word:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            hashmap.setdefault(key, []).append(strs[index])
        
        for value in hashmap.values():
            output.append(value)
        return output
            


        



            


        