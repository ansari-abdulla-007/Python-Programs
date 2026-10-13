# Adds an element.

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("Abdu")
collection.add((3, 4, 5,))

collection.remove(3)

print(collection)
print(type(collection))