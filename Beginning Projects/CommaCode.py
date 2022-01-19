def commaFunction(list):
    for i in range(len(list)-1):
        print(list[i],end=" , ")
    print("and", end=" , " )
    print(list[len(list)-1])
