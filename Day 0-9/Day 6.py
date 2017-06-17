k = int(input())
for x in range(1,k+1):
    s = input()
    m = []
    n = []
    for y in range(len(s)):
        if y  == 0:
            m.append(s[y])
        elif y % 2 ==0:
            m.append(s[y])
        elif y % 2 != 0:
            n.append(s[y])
    m = ''.join(m)
    n = ''.join(n)
    print (m, n)
            
