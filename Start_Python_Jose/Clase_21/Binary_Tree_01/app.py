from Clase_21.Binary_Tree_01.node import Node
from Clase_21.Binary_Tree_01.binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

print('\n','Inorder')
tree.inorder()
print('\n', 'Preorder')
tree.preorder()
print('\n','Postorder')
tree.postorder()
print('\n')
