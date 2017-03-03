# A generic XML to JSON converter written in Python
import xml.etree.ElementTree as ET
import json

def parseIntoJSON(node):

    x = {}

    for subelem in node:
        v = parseIntoJSON(subelem)
        key = subelem.tag
        value = v[key]

        if key not in x: # If key doesn't exist, make key-value pair
            x[key] = value
        elif isinstance(x[key], list): # If it's already an array, append to the array
            x[key].append(value)
        else: # If the key already exists but it isn't already an array, we need to convert it to an array
            x[key] = [x[key], value]

    if not x: # Base case: When there aren't sub-nodes -> Take text value
        x = node.text

    return {node.tag: x}

# Create tree from xml file
tree = ET.parse("book_list.xml")
root = tree.getroot()

# Convert XML tree to JSON
x = parseIntoJSON(root)

# Write JSON to local file
with open('parsedXML.txt', 'w') as file:
    json.dump(x, file, indent = 4)