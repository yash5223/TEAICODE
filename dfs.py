class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def dfs(root):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
def build_tree():
    value = int(input("Enter root node: "))
    root = Node(value)
    nodes = {value: root} 
    n = int(input("Enter number of nodes to add: "))
    for _ in range(n):
        parent = int(input("Enter parent node: "))
        if parent not in nodes:
            print("Parent not found, try again.")
            continue
        child = int(input("Enter child node: "))
        position = input("Left or Right? (L/R): ").strip().upper()
        child_node = Node(child)
        nodes[child] = child_node  
        if position == "L":
            nodes[parent].left = child_node
        elif position == "R":
            nodes[parent].right = child_node
        else:
            print("Invalid input. Skipping node.")
    print("\nDictionary of Nodes:")
    for key, node in nodes.items():
        left_value = node.left.value if node.left else None
        right_value = node.right.value if node.right else None
        print(f"Node: {node.value}, Left: {left_value}, Right: {right_value}")
    return root

root = build_tree()
print("\nDFS Traversal:")
dfs(root)
