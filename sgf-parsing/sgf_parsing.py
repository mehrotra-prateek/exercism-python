import re


class SgfTree(object):
    def __init__(self, properties=None, children=None):
        # print("am here")
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    """ parse input for actions"""
    __validate_input_tree(input_string)
    list_of_nodes = __list_nodes(input_string)
    if not list_of_nodes[0]:
        return SgfTree()
    else:
        property = __compute_property(list_of_nodes[0])
        child = __compute_children(list_of_nodes[1:])
        return SgfTree(properties=property, children=child)


def __compute_children(input_string):
    """ creates a list of all children nodes"""
    child = []
    for ctr in input_string:
        child.append(SgfTree(__compute_property(ctr)))
    return child


def __compute_property(input_string):
    """ creates a property in the form of dict with list"""
    ctr = 0
    char = ""
    prop = {}
    while(ctr < len(input_string)):
        char = input_string[ctr]
        while(char != "["):
            _property_key = ""
            _property_value = []
            if re.match(r"[a-z]", char):
                raise ValueError("key cannot be lower case")
            else:
                _property_key += char
                ctr += 1
                char = input_string[ctr]
        if char == "[":
            _property_values = []
        ctr += 1
        char = input_string[ctr]
        while(char != "]"):
            if char == "\\":
                ctr += 1
                char = input_string[ctr]
            _property_values.append(char.replace("\t", " "))
            ctr += 1
            char = input_string[ctr]
        _property_value.append(r"".join(_property_values))
        prop[_property_key] = _property_value
        ctr += 1
    return prop


def __list_nodes(input_string):
    """ if input string is valid then create a list of nodes"""
    list_of_nodes = re.sub(r'\(|\)', "", input_string[2:-1]).split(";")
    return list_of_nodes


def __validate_input_tree(input_string):
    """ validats the provided string """
    if not input_string[0:2] == "(;" or len(list(input_string[2:-1])) == 1:
        raise ValueError("Input is not a valid tree")
