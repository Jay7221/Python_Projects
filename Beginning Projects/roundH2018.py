def get_num_seq(N, P):
    w_seq_n = 2 ** N
    seq_dict = dict()
    for i in range(P):
        f_seq = input()
        flag = False
        for seq in seq_dict.keys():
            if len(seq) <= len(f_seq):
                if f_seq.startswith(seq):
                    flag = True
                    pass
                    
            else:
                if seq.startswith(f_seq):
                    del seq_dict[seq]
                    seq_dict[f_seq] = 2 ** (N - len(f_seq))
                    flag = True
        if flag == False:
            seq_dict[f_seq] = 2 ** (N - len(f_seq))
    for i in seq_dict.values():
        w_seq_n -= i
    return w_seq_n

T = int(input())
for j in range(T):
    N, P = input().split()
    N = int(N)
    P = int(P)
    w_seq = get_num_seq(N, P)
    print("Case #%s: %s"%(j + 1, w_seq))
    

            
        
    
    
