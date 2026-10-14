items = ("pen","pencil","eraser")
y = list(items)
y[1] = "marker"
items = tuple(y)
print(items)