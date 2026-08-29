class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        l, r = 0, len(s) - 1

        while l < r:

            if s[l] != s[r]:
                if is_palindrome(s[l + 1:r + 1]) or is_palindrome(s[l:r]):
                    return True
                else:
                    return False
            l += 1
            r -= 1

        return True
            
            
