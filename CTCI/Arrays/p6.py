# Implement a method to perform basic string compression using the counts

def compress(s):
    ret = ""
    i = 0
    while i < len(s):
        count = 1
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                count += 1
                i += 1
            else:
                break
        unit = s[i]
        unit += str(count)
        ret += unit
        i += 1

    if len(ret) > len(s):
        return s
    else:
        return ret


if __name__ == "__main__":
    s = "aabcccccaaa"
    print(compress(s))