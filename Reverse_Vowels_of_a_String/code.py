def reverse_vowels(s):
    # Define the set of vowels
    vowels = set('aeiouAEIOU')
    
    # Convert string to a list to allow modification
    s_list = list(s)
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move the left pointer to the right until a vowel is found
        while left < right and s_list[left] not in vowels:
            left += 1
        
        # Move the right pointer to the left until a vowel is found
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        # Swap the vowels
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    # Convert the list back to a string and return
    return ''.join(s_list)

# Example usage
s = "hello world"
reversed_vowels = reverse_vowels(s)
print(reversed_vowels)  # Output: "holle werld"

s2 = "leetcode"
reversed_vowels2 = reverse_vowels(s2)
print(reversed_vowels2)  # Output: "leotcede"
