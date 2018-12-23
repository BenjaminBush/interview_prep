def parse_space(string, index):
    return " "

def parse_upper(string, index):
    ascii = string[index:index+2]
    return chr(int(ascii))

def parse_lower_two(string, index):
    ascii = string[index:index+2]
    return chr(int(ascii))

def parse_lower_three(string, index):
    ascii = string[index:index+3]
    return chr(int(ascii))

def decode(encoded):
    # Write your code here
    ret = ""
    rev = ''.join(reversed(encoded))
    i = 0
    while i < len(rev) - 1:
        curr = int(rev[i])
        if curr == 3:
            s = parse_space(rev, i)
            i += 2
        elif curr >= 6:
            next = rev[i+1]
            if next == 0:
                s = parse_upper(rev, i)
                i += 2
            else:
                s = parse_lower_two(rev, i)
                i += 2
        else:
            s = parse_lower_three(rev, i)
            i += 3
        ret += s

    return ret

# sample_input = "23511011501782351112179911801562340161171141148"
# decoded = decode(sample_input)
# print(decoded)



def missingWords(s, t):
    # Write your code here
    words_S = s.split(" ")
    words_T = t.split(" ")
    t_pointer = 0
    missing_words = []
    for s_pointer in range(len(words_S)):
        if t_pointer < len(words_T):
            if words_S[s_pointer] == words_T[t_pointer]:    # We're in a subsequence, increment both
                t_pointer += 1
            else:
                missing_words.append(words_S[s_pointer])
        else:
            missing_words += words_S[s_pointer:]
            return missing_words


    return missing_words



# s = "I am using hackerrank to improve programming"
# t = "am hackerrank to improve"
# s = "I am a programmer am I"
# t = "am programmer"
#
#
#
# mW = missingWords(s, t)
# print(mW)


