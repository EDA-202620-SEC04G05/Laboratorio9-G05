from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_higher_value(father_node,child_node):
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

def default_compare_lower_value(father_node,child_node):
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)

def new_heap(is_min_pq=True):
    heap = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": None,
    }
    al.add_last(heap["elements"], pqe.new_pq_entry(None, None))
    if is_min_pq:
        heap["cmp_function"] = default_compare_lower_value
    else:
        heap["cmp_function"] = default_compare_higher_value
    return heap

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return size(my_heap) == 0

def priority(my_heap,father,child):
    return my_heap["cmp_function"](father,child)

def exchange(my_heap,i,j):
    elements = my_heap["elements"]
    temp = al.get_element(elements, i)
    al.change_info(elements, i, al.get_element(elements, j))
    al.change_info(elements, j, temp)

def swim(my_heap,pos):
    elements = my_heap["elements"]
    while pos > 1:
        father_pos = pos // 2
        father = al.get_element(elements,father_pos)
        child = al.get_element(elements, pos)
        if priority(my_heap,father,child):
            break
        exchange(my_heap,father_pos,pos)
        pos = father_pos

def insert(my_heap, priority_value, value):
    entry = pqe.new_pq_entry(priority_value, value)
    al.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"])
    return my_heap

def sink(my_heap,pos):
    elementos = my_heap["elements"]
    n = size(my_heap)
    while 2 * pos <= n:              
        hijo_pos = 2 * pos          
        if hijo_pos < n:          
            izq= al.get_element(elementos,hijo_pos)
            der = al.get_element(elementos,hijo_pos + 1)
            if not priority(my_heap, izq,der):
                hijo_pos += 1       
        padre = al.get_element(elementos, pos)
        hijo = al.get_element(elementos,hijo_pos)
        if priority(my_heap, padre,hijo):
            break                   
        exchange(my_heap, pos,hijo_pos)
        pos = hijo_pos
        
def remove(my_heap):
    if is_empty(my_heap):
        return None
    elementos = my_heap["elements"]
    primero = al.get_element(elementos,1)
    exchange(my_heap,1,size(my_heap))
    al.remove_last(elementos)
    my_heap["size"] -= 1
    sink(my_heap,1)
    return pqe.get_value(primero)


def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    primero = al.get_element(my_heap["elements"],1)
    return pqe.get_value(primero)


def is_present_value(my_heap,value):
    elementos = my_heap["elements"]
    for pos in range(1,size(my_heap) + 1):
        entrada = al.get_element(elementos,pos)
        if pqe.get_value(entrada) == value:
            return pos
    return -1


def contains(my_heap,value):
    return is_present_value(my_heap,value) != -1


def improve_priority(my_heap,prioridad,value):
    pos = is_present_value(my_heap,value)
    if pos != -1:
        entrada = al.get_element(my_heap["elements"],pos)
        pqe.set_priority(entrada,prioridad)
        swim(my_heap,pos)
    return my_heap