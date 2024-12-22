
def expand(n):
    r = ""
    i = 0
    cnt = 0
    while i < len(n):
        c = n[i]
        while i < len(n) and n[i] == c:
            i += 1
            cnt += 1

        r += str(cnt)
        r += c
        cnt = 0

    return r

l = '1113222113'
for i in range(40):
    l = expand(l)

print("1:", len(l)) 

l2 = '1113222113'
for i in range(50):
    l2 = expand(l2)

print("2:", len(l2))