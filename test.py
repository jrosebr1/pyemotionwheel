# import the necessary packages
from anytree.importer import JsonImporter
from anytree import RenderTree
from anytree import search

importer = JsonImporter()
tree = importer.import_(open("emotion_wheel_tree.json").read())
print(RenderTree(tree))

#results = search.findall(tree, filter_=lambda node: node.foo in ("root"),)
#print(results)