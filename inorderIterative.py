def inorderIterative(tree):
    stack, result = [], []
    
    while stack or tree:
        if tree:
            stack.apppend(tree)
            #Go to the left subtree
            tree = tree.left
        else:
            #Go up in the tree
            tree = stack.pop()
            result.append(tree.data)
            #Go to the right subtree
            tree = tree.right
    return result
