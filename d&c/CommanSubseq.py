def lonestCommanSubsequence(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    elif s1[index1] == s2[index2]:
        return 1 + lonestCommanSubsequence(s1, s2, index1 + 1, index2 + 1)
    else:
        op1 = lonestCommanSubsequence(s1, s2, index1 + 1, index2)
        op2 = lonestCommanSubsequence(s1, s2, index1, index2 + 1)
        return max(op1, op2)


print(lonestCommanSubsequence("elephant", "eretpat", 0, 0))
