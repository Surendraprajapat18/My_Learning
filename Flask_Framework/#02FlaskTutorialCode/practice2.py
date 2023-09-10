for _ in range(int(input())):
    s = int(input())
    b = str(input())
    f = ''
    r = 'ATCG'
    for i in range(s//2):
        d = b[i*2:i*2+2]
        if d=='00':
            f=f+r[0]
        elif d=='01':
            f=f+r[1]
        elif d=='10':
            f=f+r[2]
        elif d=='11':
            f=f+r[3]
    
    print(f)
    