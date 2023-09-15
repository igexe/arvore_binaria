def search_arvore(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    for child in node.children:
        if search_arvore(child, target):
            return True
    return False
