def lps(s, startindex, endindex):
    if startindex > endindex:
        return 0
    elif startindex == endindex:
        return 1
    elif s[startindex] == s[endindex]:
        return 2 + lps(s, startindex + 1, endindex - 1)
    else:
        option1 = lps(s, startindex, endindex - 1)
        option2 = lps(s, startindex + 1, endindex)
        return max(option1, option2)


print(lps("ELRMENMET", 0, 8))
# Output: 5 (Length of Longest Palindromic Substring starting from index)
