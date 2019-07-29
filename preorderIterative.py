def preorderIterative(tree):
    stack, result = [tree], []
    
    while stack:
        curr = stack.pop()
        if curr:
            result.append(curr.data)
            #Order in which we append the nodes in the stack matters here, we add 1st right node and then left node
            stack += [curr.right, curr.left]
   return result
    
