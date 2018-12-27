# Given two strings, write a method to decide if one is a permutation of the other (same characters, just in different order)

def check_permutation(s1, s2):
    s1_map = {}
    for char in s1:
        if char in s1_map:
            s1_map[char] += 1
        else:
            s1_map[char] = 1
    for char in s2:
        if char in s1_map:
            if s1_map[char] > 0:
                s1_map[char] -= 1
            else:
                return False
        else:
            return False

    return True

if __name__ == "__main__":
    s1 = "racecar"
    s2 = "carrace"
    print(check_permutation(s1, s2))