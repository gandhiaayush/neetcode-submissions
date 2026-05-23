class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char_string = []
        palindrome_string = []

        for char in s:
            if not char.isalnum():
                continue
            char_string.append(char)
             

        for i in range(len(char_string) - 1, -1, -1):
            char = char_string[i]
            if not char.isalnum(): 
                continue
            palindrome_string.append(char)

        if char_string == palindrome_string:
            return True

        return False



        