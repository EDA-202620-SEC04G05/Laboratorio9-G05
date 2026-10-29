from DataStructures.Tree import bst_node as bn
from DataStructures.List import single_linked_list as sl

def new_map():
    return {"root": None}

def default_compare(key, element):
    element_key = bn.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1

def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def size(my_bst):
    root = my_bst["root"]
    return size_tree(root)

def insert_node(root, key, value):
    if root is None:
        return bn.new_node(key, value)

    comp = default_compare(key, root)
    if comp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif comp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value   

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root
def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def get_node(root,key):
    if root is None:
        return None
    comp = default_compare(key,root)
    if comp < 0:
        return get_node(root['left'],key)
    elif comp >0:
        return get_node(root['right'],key)
    else:
        return root

def get(my_bst,key):
    root = my_bst["root"]
    valor_llave = get_node(root,key)
    if valor_llave is None:
        return None
    return bn.get_value(valor_llave)
    
def contains(my_bst, key):
    return get_node(my_bst["root"], key) is not None

def get_min_node(root):
    if root is None:
        return None
    elif root['left'] is None:
        return root['key']
    else:
        return get_min_node(root['left'])

def get_min(my_bst):
    root = my_bst['root']
    return get_min_node(root)

def get_max_node(root):
    if root is None:
        return None
    elif root['right'] is None:
        return root['key']
    else:
        return get_max_node(root['right'])

def get_max(my_bst):
    root = my_bst['root']
    return get_max_node(root)
def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def key_set_tree(root, key_list):
    if root is None:
        return key_list
    key_set_tree(root["left"], key_list)
    sl.add_last(key_list, root["key"])
    key_set_tree(root["right"], key_list)
    return key_list

def key_set(my_bst):
    key_list = sl.new_list()
    return key_set_tree(my_bst["root"], key_list)

def value_set_tree(root, value_list):
    if root is None:
        return value_list
    value_set_tree(root["left"], value_list)
    sl.add_last(value_list, root["value"])
    value_set_tree(root["right"], value_list)
    return value_list

def value_set(my_bst):
    value_list = sl.new_list()
    return value_set_tree(my_bst["root"], value_list)

def is_empty(my_bst):
    return my_bst["root"] is None

def keys_range(root,key_initial,key_final,list_key):
    if root is None:
        return list_key
    if root["key"] > key_initial:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(list_key, root["key"])
    if root["key"] < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)
    return list_key

def keys(my_bst, key_initial, key_final):
    key_list = sl.new_list()
    return keys_range(my_bst["root"], key_initial, key_final, key_list)

def values_range(root,key_initial,key_final,list_value):
    if root is None:
        return list_value
    if root["key"] > key_initial:
        values_range(root["left"], key_initial, key_final, list_value)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(list_value, root["value"])
    if root["key"] < key_final:
        values_range(root["right"], key_initial, key_final, list_value)
    return list_value

def values(my_bst,key_initial, key_final):
    value_list = sl.new_list()
    return values_range(my_bst["root"], key_initial, key_final, value_list)
    
    
def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def height(my_bst):
    return height_tree(my_bst["root"])