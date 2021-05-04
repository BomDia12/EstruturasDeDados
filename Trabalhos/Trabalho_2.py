def insert_weigths(weights, wookies, left_over):
    if not weights:
        return wookies, left_over

    for wookie in wookies:
        if weights[0] <= wookie[-1]:
            wookie.append(weights.pop(0))
            return insert_weigths(weights, wookies, left_over)
    left_over.append(weights.pop(0))
    return insert_weigths(weights, wookies, left_over)


n = int(input())
weights = [int(value) for value in input().split()]
wookies = [[weights.pop(0)] if weights else [] for i in range(n)]
wookies, left_over = insert_weigths(weights, wookies, [])
wookies = sorted(wookies, key=lambda x: sum(x), reverse=True)
print(' '.join([str(wookie) for wookie in wookies]) if wookies else 'Os Wookies foram para o lado sombrio da força!')
print(' '.join([str(item) for item in left_over]) if left_over else 'A força está com os Wookies!')
