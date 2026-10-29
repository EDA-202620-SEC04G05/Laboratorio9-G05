def new_list():
    newlist = {
        "elements": [],
        "size" : 0,
        
    }
    return newlist

def get_element(my_list, index): 
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1
    
def add_first(arr,element):
    arr["elements"].insert(0, element)
    arr["size"] += 1
    return arr

def add_last(arr,element):
    arr["elements"].append(element)
    arr["size"] += 1
    return arr
    
def size(arr):
    return arr["size"]
    
def first_element(arr):
    return arr["elements"][0]
def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    return my_list["elements"][my_list["size"] - 1]

def delete_element(my_list, index):
    del my_list["elements"][index]
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] > 0:
        elemento = my_list["elements"][0]
        del my_list["elements"][0]
        my_list["size"] -= 1
    return elemento

def remove_last(my_list):
    if my_list["size"] > 0:
        elemento = my_list["elements"][my_list["size"] - 1]
        del my_list["elements"][my_list["size"] - 1]
        my_list["size"] -= 1
    return elemento

def insert_element(my_list, element, index):
    my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, index, info):
    my_list["elements"][index] = info
    return my_list

def exchange(my_list, index1, index2):
    temp = my_list["elements"][index1]
    my_list["elements"][index1] = my_list["elements"][index2]
    my_list["elements"][index2] = temp
    return my_list

def sub_list(my_list, index, num_elements):
    sublist = my_list["elements"][index : index + num_elements]
    newlist = {
        "elements": sublist,
        "size": len(sublist),
    }
    return newlist

def default_sort_criteria(element1,element2):
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted

def insertion_sort(my_list, sort_crit):
    elements = my_list["elements"]
    n = size(my_list)
    for i in range(n):
        key = get_element(my_list, i)
        j = i
        while j > 0 and not sort_crit(elements[j-1], key):
            elements[j] = elements[j-1]
            j -= 1
        elements[j] = key
    return my_list

def selection_sort(my_list, default_sort_criteria):
    lista = my_list["elements"]
    tamaño = my_list["size"]
    if tamaño >= 2:
        for i in range(tamaño):
            m = i
            for j in range(i + 1, tamaño):
                if default_sort_criteria(lista[j], lista[m]):
                    m = j
            if m != i:
                exchange(my_list, i, m)
    return my_list

def shell_sort(my_list, default_sort_criteria):
    tamaño = size(my_list)
    gap = tamaño // 2
    if tamaño >= 2:
       while gap > 0:
            for i in range(gap, tamaño):
                j = i
                while j >= gap and not default_sort_criteria(get_element(my_list, j-gap), get_element(my_list, j)):
                    exchange(my_list, j-gap, j)
                    j -= gap
            gap //= 2
    return my_list
        
def merge_sort(my_list, default_sort_criteria):
    tamaño = size(my_list)
    if tamaño <= 1:
        return my_list
    medio = tamaño // 2
    izquierda = sub_list(my_list,0,medio)
    derecha = sub_list(my_list,medio,tamaño-medio)
    izquierda = merge_sort(izquierda,default_sort_criteria)
    derecha = merge_sort(derecha,default_sort_criteria)
    i = 0
    j = 0
    k = 0

    while i < izquierda["size"] and j < derecha["size"]:
        if default_sort_criteria(izquierda["elements"][i], derecha["elements"][j]):
            my_list["elements"][k] = izquierda["elements"][i]
            i += 1
        else:
            my_list["elements"][k] = derecha["elements"][j]
            j += 1
        k += 1

    while i < izquierda["size"]:
        my_list["elements"][k] = izquierda["elements"][i]
        i += 1
        k += 1

    while j < derecha["size"]:
        my_list["elements"][k] = derecha["elements"][j]
        j += 1
        k += 1

    return my_list

def quick_sort(lst, df, lo=None, hi=None):
    if lo is None and hi is None:
        lo = 0
        hi = size(lst)

    if lo >= hi:
        return lst

    pivote = hi-1

    i = lo-1
    j = lo

    while hi-1 > j: 
        if df(get_element(lst, j), get_element(lst, pivote)):
            i += 1
            exchange(lst, i, j) 
        j += 1
    exchange(lst, pivote, i+1)
    pivote = i+1

    izquierda = quick_sort(lst, df, lo, pivote)
    derecha = quick_sort(lst, df,pivote+1, hi)

    return lst
  



