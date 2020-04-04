from treelib import Node, Tree
import pprint
import json

tree = Tree()
# def create_node(self, tag=None, identifier=None, parent=None, data=None):
tree.create_node("Harry", "harry", data=1)  # root node
tree.create_node("Jane", "jane", parent="harry", data=2)
tree.create_node("Bill", "bill", parent="harry", data=8)
tree.create_node("Diane", "diane", parent="jane", data=9)
tree.create_node("Mary", "mary", parent="diane", data=7)
tree.create_node("Mark", "mark", parent="jane", data=5)

tree.show()

# print(tree.to_json(with_data=True))

pprint.pprint(tree.to_dict(with_data=True))
