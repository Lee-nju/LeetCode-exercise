while 1:
    s = input()
    if s != '':
        N, M, P, Q = [int(x) for x in s.split()]
        meituan_map = []
        xi = xj = 0
        for i in range(N):
            s = input()
            if 'S' in s:
                xi = i
                xj = s.index('S')
            meituan_map.append(list(s))

        steps = input()
        score = 0
        for s in steps:
            if s == 'W' and xi > 0 and meituan_map[xi - 1][xj] != '#':
                xi -= 1
            elif s == 'S' and xi < N - 1 and meituan_map[xi + 1][xj] != '#':
                xi += 1
            elif s == 'A' and xj > 0 and meituan_map[xi][xj - 1] != '#':
                xj -= 1
            elif s == 'D' and xj < M - 1 and meituan_map[xi][xj + 1] != '#':
                xj += 1

            if meituan_map[xi][xj] == 'O':
                score += P
                meituan_map[xi][xj] = '+'
            elif meituan_map[xi][xj] == 'X':
                score -= Q
                meituan_map[xi][xj] = '+'

        print(score)
    else:
        break
