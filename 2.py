#String matching naive algorithm
#add Wildcard ( . )

string="abcaabacabaabaca"
pattern=".aca"


def find(string, p):
    s=len(string)
    p=len(pattern)
    for i in range(s-p):
        for j in range(p):
            if pattern[j]=='.':
                continue
            if string[i+j]!=pattern[j]:
                break
        else:
            print(i)


find(string, pattern)