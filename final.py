# String matching naive algorithm
# add Wildcard ( . )
# add Optional character ( ? )
# add caret ( ^ ) symbol
# add The Escape Symbol (  \  )

string = "abcd"
pattern = "ab?cd"


def matched(string, pattern):
    s = len(string)
    p = len(pattern)

    # if pattern is Empty
    if not p:
        return True

    i = 0
    while True:
        # Escape Symbol (  \  )
        if i < p and i < s and pattern[i] == "\\":
            if string[i] == pattern[i+1]:
                if matched(string[i+1:], pattern[i+2:]):
                    return True
        # Optional character ( ? )
        if i+1 < p and pattern[i+1] == '?':
            # with this character
            option1 = matched(string[i:], pattern[i]+pattern[i+2:])
            # without this character
            option2 = matched(string[i:], pattern[i+2:])
            if option1 or option2:
                return True
            else:
                return False

        # Wildcard ( . )
        if i < p and pattern[i] == '.':
            i += 1
            continue

        if p <= i:
            return True
        if s <= i:
            return False
        if string[i] != pattern[i]:
            return False
        i += 1


def find(string, pattern):
    s = len(string)
    p = len(pattern)
    if pattern[0] == '^':
        if matched(string, pattern[1:]):
            print(0)
    else:
        for i in range(s):
            if matched(string[i:], pattern):
                print(i,end="\n")


find(string, pattern)
