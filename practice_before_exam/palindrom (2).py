"""
The Longest Palindromic Subsequence (LPS) problem is finding 
the longest subsequences of a string that is also a palindrome.
"""

from zad2ktesty import runtests


def if_pali(string):
    if string[::-1] == string:
        return True
    return False


def palindrom(S):
    n = len(S)
    DP = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        DP[i][i] = 1

    maxi = 0
    for s in range(n):
        for e in range(s + 1, n):
            if if_pali(S[s: e]):
                DP[s][e] = max(len(S[s: e]), DP[s][e - 1])
            else:
                DP[s][e] = DP[s][e - 1]
        if DP[s][e] > maxi:
            maxi = DP[s][e]
            idx = s

    output = S[idx:idx + maxi]

    return output


runtests ( palindrom )

#S = "aacaccabcc"

# acca
# 4
#print(palindrom(S))
