# Given two strings, write a function to check if they are at most n edits away

def edits_away(s1, s2, n):
    dist = edit_dist(s1, s2)
    return dist <= n

def edit_dist(s1, s2):
    memo = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            # If first string is empty, fill up with remaining length of s2
            if i == 0:
                memo[i][j] = j
            elif j == 0:
                memo[i][j] = i
            elif s1[i-1] == s2[j-1]: # If they have the same last char, then num edits will be same as substring[:-1]
                memo[i][j] = memo[i-1][j-1]
            else: # different last character, pick the min cost of replacing/inserting/deleting
                memo[i][j] = 1 + min(
                    memo[i-1][j-1],
                    memo[i-1][j],
                    memo[i][j-1]
                )

    return memo[len(s1)][len(s2)]


print(edits_away("wednesday", "thursday", 5))