from main import Node, BST


tree = BST()
tree.add(0)


tree.fill()

tree.add(5)
tree.printTree(tree.head)
print tree.deleteNode(0)
print "HEAD", tree.head.val
print tree.searchNode(0, tree.head)
print tree.isValid(tree.head, float('inf')*-1, float('inf'))
# print "COUNT:", tree.count(tree.head)
# maxNode = tree.searchMax(tree.head)
# print maxNode.val
# print tree.deleteNode(maxNode.val, tree.head)

# print tree.isValid(tree.head, float('inf')*-1, float('inf'))
# print tree.searchMin(tree.head)
# print tree.searchMax(tree.head)
# print test.head.val
# print tree.count(tree.head)

# print tree.getSuccessor(10)