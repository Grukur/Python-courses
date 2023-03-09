from Clase_21.Binary_Tree_02.node import Node
from Clase_21.Binary_Tree_02.binary_tree import BinaryTree


tree = BinaryTree(Node(6))
nodes = [5, 3, 9, 7, 8, 7.5, 12, 11, 24, 15, 17]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)

print('\n', 'Inorder')
tree.inorder()
print('\n', 'Preorder')
tree.preorder()
print('\n', 'Postorder')
tree.postorder()
print('\n')

print(tree.find(11))
