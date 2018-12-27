# Given a string, write a function to check if it is a parmutation of a palindrome

# if it is a permutation of a palindrome, then it must be possible to make a palindrome out of this string
# therefore, we just need to check if you cna make a palindrome --> equal number of chars except for one

def palindrome_permutation(s):
    map = {}
    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    num_odds = 0
    for _, k in enumerate(map):
        v = map[k]
        if v%2 == 1:
            num_odds += 1
        if num_odds > 1:
            return False
    return True


if __name__ == "__main__":
    s1 = "racecar"
    s2 = "racecarr"
    print(palindrome_permutation(s1))
    print(palindrome_permutation(s2))