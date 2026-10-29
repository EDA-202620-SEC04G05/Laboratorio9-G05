from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_higher_value(father_node,child_node):
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

def default_compare_lower_value(father_node,child_node):
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)

def new_heap(is_min_pq):
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