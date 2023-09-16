# String matching naive algorithm
# add Wildcard ( . )
# add Optional character ( ? )

string = "avvvva"
pattern = "vv?"


def matched(string, pattern):
    s = len(string)
    p = len(pattern)

    # if pattern is Empty
    if not p:
        return True

    i = 0
    while True:
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
    for i in range(s):
        if matched(string[i:], pattern):
            print(i)


find(string, pattern)
