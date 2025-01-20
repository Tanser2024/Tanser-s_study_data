def longestPalindrome( s):
    length = len(s)
    if length == 1:
        return s[0]
    l = 0
    string = ""
    for i in range(length):
        for j in range(length - 1, i - 1, -1):
            if s[i] == s[j]:
                if all(s[i + k] == s[j - k] for k in range((j - i +1)// 2)):
                    if j - i + 1 > l:
                        l = j - i + 1
                        string = s[i:j + 1]
                    break
    return string
s=input()
print(longestPalindrome(s))