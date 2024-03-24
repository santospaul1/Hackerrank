def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            # Try removing either the left or the right character
            if is_palindrome(s[i + 1:n - i]):
                return i
            elif is_palindrome(s[i:n - 1 - i]):
                return n - 1 - i
    return -1

s = 'aaab'
t = 'baa'
u = 'aaa'
print(palindromeIndex(s))  
print(palindromeIndex(t))   
print(palindromeIndex(u)) 
