import sys
t = sys.stdin.readline()
for _ in range(int(t)):
    kx,ky = map(int, sys.stdin.readline().strip().split())
    king_moves = [(kx-1,ky-1),(kx-1,ky),(kx-1,ky+1),
         (kx,ky-1),  (kx,ky+1),
         (kx+1,ky-1), (kx+1,ky), (kx+1,ky+1)]
    i=0
    while i<len(king_moves):
        if 1<=king_moves[i][0]<=8 and 1<=king_moves[i][1]<=8:
            pass
        else:
            king_moves.pop(i)
            i-=1
        i+=1
    r1x,r1y = map(int, sys.stdin.readline().strip().split())
    r1_moves = [(r1x,ky),(kx,r1y)]
    r2x,r2y = map(int, sys.stdin.readline().strip().split())
    r2_pos,r1_pos=(r2x,r2y),(r1x,r1y)
    r2_moves = [(r2x,ky),(kx,r2y)]
    checkmate = False

    if  len(king_moves)>5:
        print("NO")
        continue
    if r1x==r2x:
        if r1x>kx and r2x>kx:
            if r1y>r2y:
                r1_moves[0] =(0,0)
            else:
                r2_moves[0] =(0,0)
        elif r1x<kx and r2x<kx:
            if r1y>r2y:
                r2_moves[0] =(0,0)
            else:
                r1_moves[0] =(0,0)
    if r1y==r2y:
        if r1x>kx and r2x>kx:
            if r1x>r2x :
                r1_moves[1] = (0,0)
            else:
                r2_moves[1] = (0,0)
        else:
            if r1x>r2x :
                r2_moves[1] = (0,0)
            else:
                r1_moves[1] = (0,0)


    for i in range(len(r1_moves)):
        sum1 = 0
        sum2 = 0
        for j in king_moves:
            if ((r1_moves[i][0]==j[0] or r1_moves[i][1]==j[1]) and r1_moves[i]!=j) or (j[0]==r2x or j[1]==r2y and (j!=r2_pos)):
                sum1+=1
            if ((r2_moves[i][0]==j[0] or r2_moves[i][1]==j[1]) and r2_moves[i]!=j) or ((j[0]==r1x or j[1]==r1y) and j!=r1_pos):
                sum2+=1
            else:
                break
        if sum1==len(king_moves) or sum2==len(king_moves):
            checkmate=True
            break        

    if checkmate:
        print("YES")
    else:
        print("NO")