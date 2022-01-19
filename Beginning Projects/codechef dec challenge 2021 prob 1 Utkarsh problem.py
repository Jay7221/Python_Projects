T = int(input())
for i in range(0, T):
    first, second, third = input().split()
    x, y = input().split()
    pref = {first:1, second:2, third:3}
    if pref[x] > pref[y]:
        print(x)
    else:
        print(y)
