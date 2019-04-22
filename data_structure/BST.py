class BSTNode(object):
    def __init__(self, val=None):
        self.val   = val
        self.left  = None
        self.right = None

class BSTree(object):
    def __init__(self, val=None):
        self.root = BSTNode(val)

    def insert(self, val, root):
        if val < root.val:
            if root.left is not None:
                self.insert(val, root.left)
            else:
                root.left = BSTNode(val)
        else:
            if root.right is not None:
                self.insert(val, root.right)
            else: 
                root.right = BSTNode(val)

    def preorder(self, root):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
         
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

         
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    def contains(self, val, root):
        if root is None:
            return False
        if val == root.val:
            return True
        elif val < root.val:
            return self.contains(val, root.left)
        else:
            return self.contains(val, root.right)
          
               
tree = BSTree(10)

print('------------------Insert A Node------------------')
tree.insert(3, tree.root)
tree.insert(19, tree.root)
tree.preorder(tree.root)

print('------------------Insert A Node------------------')
tree.insert(4, tree.root)
tree.insert(97, tree.root)
tree.preorder(tree.root)

print('------------------Insert A Node------------------')
tree.insert(2, tree.root)
tree.insert(17, tree.root)


print('------------------Pre Order-----------------------')
tree.preorder(tree.root)

print('------------------In Order-----------------------')
tree.inorder(tree.root)

print('------------------Post Order----------------------')
tree.postorder(tree.root)

print('------------------Contains------------------------')
print('tree contains 10: ', tree.contains(10, tree.root))
print('tree contains 100: ', tree.contains(100, tree.root))
print('tree contains 17: ', tree.contains(17, tree.root))
print('tree contains 2: ', tree.contains(2, tree.root))
print('tree contains 3: ', tree.contains(3, tree.root))

