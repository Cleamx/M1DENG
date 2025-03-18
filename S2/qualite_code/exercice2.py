def plus_long_palindrome(s):
    plus_long_sous_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sous_chaine = s[i:j+1]
            if is_palindrome(sous_chaine) and len(sous_chaine) > len(plus_long_sous_palindrome):
                plus_long_sous_palindrome = sous_chaine
    return plus_long_sous_palindrome

def is_palindrome(s):
    return s == s[::-1]

print(plus_long_palindrome("cbbd"))
