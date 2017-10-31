def best_path(nm, prob):
    #nm [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
    #prob [1.0, 0.9, 0.3, 0.1, 0.8, 1.0]
    res = []
    # S = []
    Q = [x for x in range(n)]
    while Q != []:
        u = Q.pop(0)
        # S.append(u)
        m = 0
        best = 0
        for v in range(len(nm[u])):
            if nm[u][v] == 1:
                if prob[v] > m:
                    m = prob[v]
                    best = v
        res.append(best)
    res = sorted(set(res))
    res = [str(x) for x in res]
    return "-".join(res)