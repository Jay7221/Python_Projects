T = int(input())
for i in range(T):
    N = int(input())
    arr = input().split()
    pair_dict = dict()
    for num in arr:
        pair_dict.setdefault(num, 0)
        pair_dict[num] += 1
    max_time = max(pair_dict.values())
    num_moves = sum(pair_dict.values()) - 1
    max_val = max(pair_dict.values())
    num_moves -= max_val // 4
    if N == 1:
        print(0)
    elif max_val // 2 < 1:
        print(-1)
    else:
        print(num_moves)
