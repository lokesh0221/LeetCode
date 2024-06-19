class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Helper function to find the greatest common divisor of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Check if str1 and str2 have a common divisor string
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The GCD string will be the prefix of str1 (or str2) up to gcd_length
        return str1[:gcd_length]


# Example usage:
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB")) # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))   # Output: ""