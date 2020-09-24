def solve(s, n, k):
    l, r = 0, n-1
    while l < n and s[l] == '0':
        l+=1
    while r > -1 and s[r] == '0':
        r-=1
    sides, mids = [l, n-1-r], []
    cnt = 0
    for i in range(l,r+1):
        if s[i] == '1':
            if cnt > 0:
                mids.append(cnt)
            cnt = 0
        else:
            cnt += 1
    res = 0
    mids.sort(reverse=True)
    # print(mids, sides)
    zeros = sum(sides) + sum(mids)
    if k >= 2*len(mids) + len(sides) or s == '0'*n:
        return 0
    if k % 2 == 1:
        zeros -= max(sides)
        sides = [min(sides)]
        k -= 1
    i = 0
    while k > 2:
        zeros -= mids[i]
        i += 1
        k -= 2
    if k == 1:
        zeros -= min(sides)
    elif k == 2:
        zeros -= max(mids[i], sum(sides))
    return zeros

for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    print(solve(s,n,k))
