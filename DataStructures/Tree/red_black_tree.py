from DataStructures.Tree import rbt_node as rb
from DataStructures.List import single_linked_list as sl

def new_map():
    return {'root':None, 'type':"RBT"}

def default_compare(key,element):
    element_key = rb.get_key(element)
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
    root = my_bst['root']
    return size_tree(root)

def flip_node_color(node_rbt):
    if node_rbt['color'] == 0:
        node_rbt['color'] = 1
    else:
        node_rbt['color'] = 0
    return node_rbt

def flip_colors(node_rbt):
    if node_rbt is not None:
        flip_node_color(node_rbt)
        if node_rbt['right'] is not None:
            flip_node_color(node_rbt['right'])
        if node_rbt['left'] is not None:
            flip_node_color(node_rbt['left'])
    
    return node_rbt

def rotate_left(node_rbt):
    right_child = node_rbt['right']
    node_rbt['right'] = right_child['left']
    right_child['left'] = node_rbt
    start_color = node_rbt['color']
    node_rbt['color'] = right_child['color']
    right_child['color'] = start_color
    right_child["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + size_tree(node_rbt["left"]) + size_tree(node_rbt["right"])
    return right_child

def rotate_right(node_rbt):
    left_child = node_rbt['left']
    node_rbt['left'] = left_child['right']
    left_child['right'] = node_rbt
    start_color = node_rbt['color']
    node_rbt['color'] = left_child['color']
    left_child['color'] = start_color
    left_child["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + size_tree(node_rbt["left"]) + size_tree(node_rbt["right"])
    return left_child

def insert_node(root, key, value):
    if root is None:
        return rb.new_node(key, value)

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    rb.change_color(my_rbt["root"], rb.BLACK)
    return my_rbt 
   
def is_red(node_rbt):
    if node_rbt is None:
        return False
    return rb.is_red(node_rbt)

def is_empty(my_rbt):
    return my_rbt["root"] is None

def get_node(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp == 0:
        return root
    elif cmp < 0:
        return get_node(root["left"], key)
    else:
        return get_node(root["right"], key)

def get(my_rbt, key):
    node = get_node(my_rbt["root"], key)
    if node is None:
        return None
    return rb.get_value(node)

def contains(my_rbt, key):
    return get_node(my_rbt["root"], key) is not None

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sl.add_last(key_list, rb.get_key(root))
        key_set_tree(root["right"], key_list)
    return key_list

def key_set(my_rbt):
    key_list = sl.new_list()
    return key_set_tree(my_rbt["root"], key_list)

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sl.add_last(value_list, rb.get_value(root))
        value_set_tree(root["right"], value_list)
    return value_list

def value_set(my_rbt):
    value_list = sl.new_list()
    return value_set_tree(my_rbt["root"], value_list)

def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return rb.get_key(root)
    return get_min_node(root["left"])

def get_min(my_rbt):
    return get_min_node(my_rbt["root"])

def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return rb.get_key(root)
    return get_max_node(root["right"])

def get_max(my_rbt):
    return get_max_node(my_rbt["root"])

def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def height(my_rbt):
    return height_tree(my_rbt["root"])