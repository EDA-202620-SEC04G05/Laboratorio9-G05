from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random
from DataStructures.List import array_list as lt
def new_map(num_elements,load_factor, prime=109345121):
    if not mf.is_prime(prime):
        prime = 109345121
    capacity = mf.next_prime(num_elements/load_factor)
    scale = random.randint(1,prime-1)
    shift = random.randint(0,prime-1)
    table = lt.new_list()
    i = 0
    while i<capacity:
        lt.add_last(table,me.new_map_entry(None,None))
        i+=1
    simbolos = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,
        'limit_factor':load_factor,
        'size':0 
            
    }
    
    return simbolos

def is_available(table,pos):
    entry = lt.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
      return 1
    return -1

def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
        hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail

def size(my_map):
    return my_map["size"]

def rehash(my_map):
    capacity = mf.next_prime(my_map["capacity"]*2)
    table = lt.new_list()
    tabla_vieja = my_map["table"]["elements"]
    i = 0
    while i<capacity:
        lt.add_last(table,me.new_map_entry(None,None))
        i+=1
    my_map["capacity"] = capacity
    for entry in tabla_vieja:
        key = me.get_key(entry)
        if key is not None and key !="__EMPTY__":
            value = me.get_value(entry)
            pos = mf.hash_value(my_map,key)
            insertado = None
            while not insertado:
                if is_available(table, pos):
                    lt.change_info(table, pos, me.new_map_entry(key, value))
                    insertado = True
                else:
                    pos = (pos + 1) % capacity
    my_map["table"] = table
    return my_map

def put(my_map,key,value):
    value_hash = mf.hash_value(my_map,key)
    ocupado, slot = find_slot(my_map,key,value_hash)
    if ocupado:
        entry = lt.get_element(my_map["table"], slot)
        me.set_value(entry, value)
    else:
        nueva_entry = me.new_map_entry(key, value)
        lt.change_info(my_map["table"], slot, nueva_entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)
    return my_map

def contains(my_map, key):
    value_hash = mf.hash_value(my_map, key)
    ocupado, slot = find_slot(my_map, key, value_hash)
    return ocupado

def get(my_map, key):
    value_hash = mf.hash_value(my_map, key)
    occupado, slot = find_slot(my_map, key, value_hash)
    if occupado:
        entry = lt.get_element(my_map["table"], slot)
        return me.get_value(entry)
    return None

def remove(my_map, key):
    value_hash = mf.hash_value(my_map, key)
    ocupado, slot = find_slot(my_map, key, value_hash)
    if ocupado:
        entry_vacia = me.new_map_entry("__EMPTY__", "__EMPTY__")
        lt.change_info(my_map["table"], slot, entry_vacia)
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map

def is_empty(my_map):
    return size(my_map)==0

def key_set(my_map):
    lista_llaves = lt.new_list()
    tabla = my_map["table"]
    tamanio = lt.size(tabla)
    for i in range(tamanio):
        entrada = lt.get_element(tabla,i)
        if entrada is not None:
            key = me.get_key(entrada)
            if key is not None and key != "__EMPTY__":
                lt.add_last(lista_llaves,key)
    return lista_llaves


def value_set(my_map):
    lista_valores = lt.new_list()
    tabla = my_map["table"]
    tamanio = lt.size(tabla)
    for i in range(tamanio):
        entrada = lt.get_element(tabla,i)
        if entrada is not None:
            key = me.get_key(entrada)
            if key is not None and key != "__EMPTY__":
                valor = me.get_value(entrada)
                lt.add_last(lista_valores,valor)
    return lista_valores


    