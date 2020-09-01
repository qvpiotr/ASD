class pokemon:
    def __init__(self):
        self.relased = False #czy wypuszczony
        self.my_prey = [] #lista na które poluje
        self.hunting_me = [] #lista które na niego poluja

def releaseThemAll(array, n):
    poke = [None] * n
    for i in range (n):
        poke[i] = pokemon()
    relase_order = [-1] * n #wynik

    for i in range (len(array)):
        predator = array[i][0]
        prey = array[i][1]
        poke[predator].my_prey.append(prey)
        poke[prey].hunting_me.append(predator)

    #wypuszczam wzystkie spokojne, lista my_prey jest pusta
    id_order = 0 #indeks w tablicy wyników
    for i in range (n):
        if len(poke[i].my_prey) == 0:
            relase_order[id_order] = i
            id_order += 1
            poke[i].relased = True

    for i in range(n):
        if poke[i].relased == False:
            release_hunters(poke, i, id_order, relase_order)
            id_order+=1
    
    if relase_order[n-1] == -1: return False
    else: return relase_order


def release_hunters(poke, index, id_order, relase_order):
    counter = 0
    for i in range (len(poke[index].my_prey)):
        id = poke[index].my_prey[i]
        if poke[id].relased == True:
            counter += 1
            if counter == 2: break
    if counter < 2: return 
    else: 
        relase_order[id_order] = index
        poke[index].relased = True
        for i in range (len(poke[index].hunting_me)):
            id = poke[index].hunting_me[i]
            id_order+=1
            release_hunters(poke, id, id_order, relase_order)



array = [(1,3),(1,0),(1,2),(5,1),(5,2),(5,4)]
n = 6
print(releaseThemAll(array,n))