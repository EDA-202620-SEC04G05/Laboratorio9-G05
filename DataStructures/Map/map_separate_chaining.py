from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
 
 
def new_map(num_elements, load_factor, prime=109345121):
    if not mf.is_prime(prime):
        prime = 109345121
    capacity = mf.next_prime(num_elements / load_factor)
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = lt.new_list()
    i = 0
    while i < capacity:
        lt.add_last(table, sl.new_list())
        i += 1
    simbolos = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    return simbolos
 
 
def size(my_map):
    return my_map["size"]
 
 
def is_empty(my_map):
    return size(my_map) == 0
 
 
def default_compare(key, element):
    if key == me.get_key(element):
        return 0
    elif key > me.get_key(element):
        return 1
    return -1
 
 
def find_in_bucket(bucket, key):
    i = 0
    n = sl.size(bucket)
    while i < n:
        entry = sl.get_element(bucket, i)
        if default_compare(key, entry) == 0:
            return i, entry
        i += 1
    return -1, None
 
 
def rehash(my_map):
    capacity = mf.next_prime(my_map["capacity"] * 2)
    tabla_vieja = my_map["table"]
    nueva_tabla = lt.new_list()
    i = 0
    while i < capacity:
        lt.add_last(nueva_tabla, sl.new_list())
        i += 1
 
    my_map["capacity"] = capacity  
    for b in range(lt.size(tabla_vieja)):
        bucket = lt.get_element(tabla_vieja, b)
        for j in range(sl.size(bucket)):
            entry = sl.get_element(bucket, j)
            pos = mf.hash_value(my_map, me.get_key(entry))
            sl.add_last(lt.get_element(nueva_tabla, pos),
                        me.new_map_entry(me.get_key(entry), me.get_value(entry)))
 
    my_map["table"] = nueva_tabla
    my_map["current_factor"] = my_map["size"] / capacity
    return my_map
 
 
def put(my_map, key, value):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], pos)
    idx, entry = find_in_bucket(bucket, key)
    if idx != -1:
        me.set_value(entry, value)
    else:
        sl.add_last(bucket, me.new_map_entry(key, value))
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
 
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)
    return my_map
 
 
def contains(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], pos)
    idx, _ = find_in_bucket(bucket, key)
    return idx != -1
 
 
def get(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], pos)
    idx, entry = find_in_bucket(bucket, key)
    if idx != -1:
        return me.get_value(entry)
    return None
 
 
def remove(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], pos)
    idx, _ = find_in_bucket(bucket, key)
    if idx != -1:
        sl.delete_element(bucket, idx)
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map
 
 
def key_set(my_map):
    lista_llaves = lt.new_list()
    tabla = my_map["table"]
    for b in range(lt.size(tabla)):
        bucket = lt.get_element(tabla, b)
        for j in range(sl.size(bucket)):
            lt.add_last(lista_llaves, me.get_key(sl.get_element(bucket, j)))
    return lista_llaves
 
 
def value_set(my_map):
    lista_valores = lt.new_list()
    tabla = my_map["table"]
    for b in range(lt.size(tabla)):
        bucket = lt.get_element(tabla, b)
        for j in range(sl.size(bucket)):
            lt.add_last(lista_valores, me.get_value(sl.get_element(bucket, j)))
    return lista_valores
