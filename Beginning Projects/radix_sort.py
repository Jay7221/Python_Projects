#! python3
# radix_sort.py

from Queue import Queue

def r_sort(num_list, digits = 3):
    bins = dict()
    main_bin = Queue()
    side_bin = Queue()
    for i in range(10):
        bins[i] = Queue()
    r = -1
    for num in num_list:
        main_bin.enqueue(num)
    while r > -digits:
        while not main_bin.is_empty():
            num = main_bin.dequeue()
            if len(str(num)) < -r:
                side_bin.enqueue(num)
                
            else:
                k = int(str(num)[r])
                bins[k].enqueue(num)
        while not side_bin.is_empty():
            main_bin.enqueue(side_bin.dequeue())
        for k in range(10):
            while not bins[k].is_empty():
                temp = bins[k].dequeue()
                main_bin.enqueue(temp)
        print(main_bin.items)
        r -= 1
        print(r)
    return main_bin.items

if __name__ == '__main__':
    
    import random
    l = list()
    for i in range(20):
        l.append(random.randrange(30))
    print(r_sort(l))
