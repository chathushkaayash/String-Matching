#String matching naive algorithm

string="abcaabacabaabaca"
pattern="aabac"


def find(string, pattern):
    s=len(string)
    p=len(pattern)
    for i in range(s-p):
        for j in range(p):
            if string[i+j]!=pattern[j]:
                break
        else:
            print(i)


find(string, pattern)