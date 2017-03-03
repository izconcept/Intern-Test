
def parseIntoJSON(filePath):
    file = open(filePath)
    x = {}
    while True:
        c = file.read(1)

        if not c:
            break

        if c == "<":
            c = file.read(1)
            if c == "!" or c == "?":
                print 'no good'
            if c == "/":
                
            else:
                key = ""
                while True:
                    c = file.read(1)
                    if(c == ">"):
                        stack.append(key)
                        break
                    else:
                        key += c



#parseIntoJSON("book_list.xml")

file = {}
file['x'] = {}
y = file['x']
y = 'das'

print file