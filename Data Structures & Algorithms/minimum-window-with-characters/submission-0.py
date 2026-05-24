import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_count = collections.Counter(t)
        need = len(t_count)
        have = 0 

        window = collections.defaultdict(int)
        best, best_length = "", float("inf")

        left = 0 
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in t_count and window[char] == t_count[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < best_length:
                    best = s[left:right + 1]
                    best_length = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        return best
            


        