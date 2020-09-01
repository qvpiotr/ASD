def bricks(tuple):
    firsts=[]
    seconds=[]

    num_of_elem=0
    for i in tuple:
        firsts.append(i[0])
        seconds.append(i[1])
        num_of_elem+=1
    
    firsts.sort()
    seconds.sort()

    max_level=1
    tmp_level=1
    i=1
    j=0
    while (i<num_of_elem and j<num_of_elem):
        if (firsts[i]<=seconds[j]):
            tmp_level+=1
            if(max_level<tmp_level):
                max_level=tmp_level
            
            if firsts[i]==seconds[j]:
                j+=1
            i+=1
        else:
            tmp_level-=1
            j+=1

    return max_level

print(bricks( [ (1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]))
print(bricks([(1,2),(1,2),(1,2),(1,2),(1,3)]))
print(bricks([(1,3),(3,5),(5,7)]))

