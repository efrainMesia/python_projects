''' Leetcode link --> https://leetcode.com/problems/palindrome-number '''
def isPalindrome(x: int) -> bool:
    temp_x = x
    reversed_x = 0
    if temp_x > 0:
        while temp_x > 0:
            reversed_x= (reversed_x*10)+ temp_x%10
            temp_x = temp_x//10
        return reversed_x == x
    return False



''' Leetcode link --> https://leetcode.com/problems/roman-to-integer/ '''
def romanToInt(s: str) -> int:
    roman_dict = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100, 'D': 500, 'M': 1000}
    total_sum = 0
    for i in range(len(s)):
        if i+1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
            total_sum-= roman_dict[s[i]]
        else:
            total_sum+= roman_dict[s[i]]
    return total_sum



'''Leetcode link --> https://leetcode.com/problems/longest-common-prefix/ '''
def longestCommonPrefix(strs) -> str:
    shortest_word = min(strs, key=len)
    i = len(shortest_word)
    while i >=0:
        count =0
        sub_shortest = shortest_word[:i]
        for word in strs:
            if sub_shortest in word[:len(sub_shortest)]:
                count +=1
        if count == len(strs):
            return shortest_word[:i]
        i-=1
    return ""











print(longestCommonPrefix(["aaa","aa","aaa"]))





