def new_list():
    newlist = {"first": None,
               "last": None,
               "size": 0}
    return newlist

def get_element(my_list, pos): 
    searchpos = 0 
    node = my_list["first"] 
    while searchpos < pos: 
        node = node["next"] 
        searchpos += 1 
    return node ["info"]

def is_present(my_list, element, cmp_function):
    temp = my_list["first"]
    count = 0
    while temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            return count
        temp = temp["next"]
        count += 1
    return -1

def is_empty(sll)->bool:
    return sll["size"] == 0
    
def add_first(sll,elemento)->dict:
    nodo = {"info": elemento,
            "next": sll["first"]}
    sll["first"] = nodo
    if sll["last"] == None:
        sll["last"] = nodo
    sll["size"] += 1
    return sll

def add_last(sll,elemento)->dict:
    nodo = {"info": elemento,
            "next": None}
    if sll["last"] == None:
        sll["first"] = nodo
    else:
        sll["last"]["next"] = nodo
    sll["last"] = nodo
    sll["size"] += 1
    return sll

def size(sll)->int:
    return sll["size"]
    
def first_element(sll)->any:
    if is_empty(sll):
        raise Exception('IndexError: list index out of range')
    else:
        elemento = sll["first"]["info"]
        return elemento
    
def last_element(sll)->any:
    if is_empty(sll):
        raise Exception('IndexError: list index out of range')
    else:
        elemento = sll["last"]["info"]
        return elemento

def delete_element(sll,posicion)->dict:
    if posicion < 0 or posicion >= size(sll):
        raise Exception('IndexError: list index out of range')
    else:
        if posicion == 0:
            sll["first"] = sll["first"]["next"]
            if sll["first"] == None:
                sll["last"] = None
        else:
            nodo_contador = sll["first"]
            for nodo in range(posicion-1):
                nodo_contador = nodo_contador["next"]
            nodo_contador["next"] = nodo_contador["next"]["next"]
            if nodo_contador["next"] == None:
                sll["last"] = nodo_contador
        sll["size"] -= 1
    return sll

def remove_first(sll)->any:
    if is_empty(sll):
        raise Exception('IndexError: list index out of range')
    else:
        elemento_eliminado = sll["first"]["info"]
        if sll["first"] == sll["last"]:
            sll["first"] = None
            sll["last"] = None
        else:
            sll["first"] = sll["first"]["next"]
        sll["size"] -= 1
    return elemento_eliminado

def remove_last(sll)->any:
    if is_empty(sll):
        raise Exception('IndexError: list index out of range')
    else:
        if sll["first"] == sll["last"]:
            elemento_eliminado = sll["first"]["info"]
            sll["first"] = None
            sll["last"] = None
        else:
            nodo_contador = sll["first"]
            while nodo_contador["next"] != sll["last"]:
                nodo_contador = nodo_contador["next"]
            elemento_eliminado = nodo_contador["next"]["info"]
            nodo_contador["next"] = None
            sll["last"] = nodo_contador
        sll["size"] -= 1
        return elemento_eliminado

def insert_element(sll,elemento,posicion)->dict:
    if posicion < 0 or posicion > size(sll):
        raise Exception('IndexError: list index out of range')
    else:
        if posicion == 0:
            add_first(sll,elemento)
        elif posicion == size(sll):
            add_last(sll,elemento)
        else:
            nodo_contador = sll["first"]
            for nodo in range(posicion-1):
                nodo_contador = nodo_contador["next"]
            nuevo_nodo = {"info": elemento,
                          "next": nodo_contador["next"]}
            nodo_contador["next"] = nuevo_nodo
            sll["size"] += 1
        return sll

def change_info(sll,posicion,nueva_info)->dict:
    if posicion < 0 or posicion >= size(sll):
        raise Exception('IndexError: list index out of range')
    else:
        nodo_contador = sll["first"]
        for nodo in range(posicion):
            nodo_contador = nodo_contador["next"]
        nodo_contador["info"] = nueva_info
    return sll

def exchange(sll,posicion1,posicion2)->dict:
    if posicion1 < 0 or posicion1 >= size(sll) or posicion2 < 0 or posicion2 >= size(sll):
        raise Exception('IndexError: list index out of range')
    else:
        nodo_pos1 = sll["first"]
        for nodo in range(posicion1):
            nodo_pos1 = nodo_pos1["next"]
        nodo_pos2 = sll["first"]
        for nodo in range(posicion2):
            nodo_pos2 = nodo_pos2["next"]
        info1 = nodo_pos1["info"]
        nodo_pos1["info"] = nodo_pos2["info"]
        nodo_pos2["info"] = info1
    return sll
def sub_list(sll,pos_inicial,num_elementos)->dict:
    if pos_inicial < 0 or pos_inicial >= size(sll) or num_elementos < 0 or pos_inicial + num_elementos > size(sll):
        raise Exception('IndexError: list index out of range')
    else:
        sublista = new_list()
        nodo_contador = sll["first"]
        for nodo in range(pos_inicial):
            nodo_contador = nodo_contador["next"]
        for nodo in range(num_elementos):
            add_last(sublista,nodo_contador["info"])
            nodo_contador = nodo_contador["next"]
    return sublista

def default_sort_criteria(element1,element2):
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list,default_sort_criteria):
    tamaño = size(my_list)
    if tamaño>=2:
        for i in range(tamaño):
            nodo_actual_elemento = my_list['first']
            for j in range(i+1,tamaño):
                nodo_sig_elemento = nodo_actual_elemento['next']
                if default_sort_criteria(nodo_actual_elemento['info'],nodo_sig_elemento['info'])==False:
                    exchange(my_list,i,j)
                nodo_actual_elemento = nodo_sig_elemento
                nodo_sig_elemento = nodo_actual_elemento['next']
    return my_list

def insertion_sort(my_list, default_sort_criteria):
    tamaño = size(my_list)
    if tamaño < 2:
        return my_list

    lista_ordenada = new_list()
    nodo_actual = my_list['first']

    while nodo_actual is not None:
        nodo_siguiente = nodo_actual['next']
        nodo_actual['next'] = None

        if lista_ordenada['first'] is None:
            lista_ordenada['first'] = nodo_actual
            lista_ordenada['last'] = nodo_actual
        else:
            nodo_busqueda = lista_ordenada['first']
            nodo_anterior = None

            while nodo_busqueda is not None and default_sort_criteria(nodo_busqueda['info'], nodo_actual['info']):
                nodo_anterior = nodo_busqueda
                nodo_busqueda = nodo_busqueda['next']

            if nodo_anterior is None:
                nodo_actual['next'] = lista_ordenada['first']
                lista_ordenada['first'] = nodo_actual
            else:
                nodo_actual['next'] = nodo_busqueda
                nodo_anterior['next'] = nodo_actual

            if nodo_busqueda is None:
                lista_ordenada['last'] = nodo_actual

        nodo_actual = nodo_siguiente

    my_list['first'] = lista_ordenada['first']
    my_list['last'] = lista_ordenada['last']
    my_list['size'] = tamaño
    return my_list

def shell_sort(my_list, default_sort_criteria):
    tamaño = size(my_list)
    if tamaño < 2:
        return my_list
    
    nodes = []
    curr = my_list["first"]
    while curr is not None:
        nodes.append(curr)
        curr = curr["next"]
        
    gap = tamaño // 2
    while gap > 0:
        for i in range(gap, tamaño):
            temp_node = nodes[i]
            j = i
            while j >= gap and not default_sort_criteria(nodes[j - gap]["info"], temp_node["info"]):
                nodes[j] = nodes[j - gap]
                j -= gap
            nodes[j] = temp_node
        gap //= 2
    for k in range(tamaño - 1):
        nodes[k]["next"] = nodes[k + 1]
    nodes[-1]["next"] = None

    my_list["first"] = nodes[0]
    if "last" in my_list:
        my_list["last"] = nodes[-1]
        
    my_list["size"] = tamaño
    return my_list

def sub_lista(my_list, start, length):
    if length <= 0:
        return {"first": None, "last": None, "size": 0}
    
    curr = my_list["first"]
    for i in range(start):
        if curr is None:
            break
        curr = curr["next"]
        
    new_first = None
    new_last = None
    count = 0
    while curr is not None and count < length:
        new_node = {"info": curr["info"], "next": None}
        if new_first is None:
            new_first = new_node
            new_last = new_node
        else:
            new_last["next"] = new_node
            new_last = new_node
        curr = curr["next"]
        count += 1
        
    return {"first": new_first, "last": new_last, "size": count}

def merge_sort(my_list, default_sort_criteria):
    tamaño = size(my_list)
    if tamaño <= 1:
        return my_list
    
    medio = tamaño // 2
    izquierda = sub_lista(my_list, 0, medio)
    derecha = sub_lista(my_list, medio, tamaño - medio)
    
    izquierda = merge_sort(izquierda, default_sort_criteria)
    derecha = merge_sort(derecha, default_sort_criteria)
    
    i = 0
    j = 0
    
    p_izq = izquierda["first"]
    p_der = derecha["first"]
    
    dummy = {"info": None, "next": None}
    curr = dummy

    while i < izquierda["size"] and j < derecha["size"]:
        if default_sort_criteria(p_izq["info"], p_der["info"]):
            curr["next"] = p_izq
            p_izq = p_izq["next"]
            i += 1
        else:
            curr["next"] = p_der
            p_der = p_der["next"]
            j += 1
        curr = curr["next"]

    while i < izquierda["size"]:
        curr["next"] = p_izq
        p_izq = p_izq["next"]
        i += 1
        curr = curr["next"]

    while j < derecha["size"]:
        curr["next"] = p_der
        p_der = p_der["next"]
        j += 1
        curr = curr["next"]

    my_list["first"] = dummy["next"]
    
    last_node = my_list["first"]
    while last_node and last_node["next"]:
        last_node = last_node["next"]
        
    if "last" in my_list:
        my_list["last"] = last_node
        
    my_list["size"] = tamaño
    return my_list

def quick_sort(my_list, default_sort_criteria):
    tamaño = size(my_list)
    if tamaño < 2:
        return my_list
    
    nodes = []
    curr = my_list["first"]
    while curr is not None:
        nodes.append(curr)
        curr = curr["next"]
    
    def quicksort(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)
            
    def partition(low, high):
        pivot_node = nodes[high]
        pivot_info = pivot_node["info"]
        i = low - 1
        
        for j in range(low, high):
            if not default_sort_criteria(pivot_info, nodes[j]["info"]):
                i += 1
                nodes[i], nodes[j] = nodes[j], nodes[i]
                
        nodes[i + 1], nodes[high] = nodes[high], nodes[i + 1]
        return i + 1

    quicksort(0, tamaño - 1)
    
    for k in range(tamaño - 1):
        nodes[k]["next"] = nodes[k + 1]
    nodes[-1]["next"] = None
    
    my_list["first"] = nodes[0]
    if "last" in my_list:
        my_list["last"] = nodes[-1]
    my_list["size"] = tamaño
    
    return my_list



    
    