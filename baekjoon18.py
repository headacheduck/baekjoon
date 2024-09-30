H, M = map(int,input().split())

if M >= 45 :
    after_M = M - 45
    print(H, after_M)

if M < 45 :
    after_H = H - 1 
    after_M = 60+(M-45)

    if after_H == -1 :
        print(int(after_H + 24), after_M)
        
    else :
        print(after_H, after_M)