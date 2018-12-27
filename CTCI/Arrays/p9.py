# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring

def str_rotation(s1, s2):
    big_s1 = s1+s1
    return s2 in big_s1

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(str_rotation(s1, s2))