import xml.etree.ElementTree as ET
import pprint

def parseIntoJSON(node):

    x = {}

    for subelem in node:
        v = parseIntoJSON(subelem)
        tag = subelem.tag
        value = v[tag]
        try:
            x[tag].append(value)
        except KeyError: #
           x[tag] = value
        except AttributeError:
            x[tag] = [x[tag], value]

    if not x:
        x = node.text
    return {node.tag: x}

tree = ET.parse("book_list.xml")
root = tree.getroot()
x = parseIntoJSON(root)

printer = pprint.PrettyPrinter(indent=4)
printer.pprint(x)