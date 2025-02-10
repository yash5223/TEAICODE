from queue import Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def bfs(root):
    if not root:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.value, end=" ")
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
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
        nodes[child] = child_node  # Store child node
        # Link child to parent
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
print("\nBFS Traversal:")
bfs(root)


'''
OUTPUT:-
Enter root node: 1
Enter number of nodes to add: 6
Enter parent node: 1
Enter child node: 2
Left or Right? (L/R): L
Enter parent node: 1
Enter child node: 3
Left or Right? (L/R): R
Enter parent node: 2
Enter child node: 4
Left or Right? (L/R): R
Enter parent node: 3
Enter child node: 7
Left or Right? (L/R): R
Enter parent node: 4
Enter child node: 5
Left or Right? (L/R): L
Enter parent node: 4
Enter child node: 6
Left or Right? (L/R): R

Dictionary of Nodes:
Node: 1, Left: 2, Right: 3
Node: 2, Left: None, Right: 4
Node: 3, Left: None, Right: 7
Node: 4, Left: 5, Right: 6
Node: 7, Left: None, Right: None
Node: 5, Left: None, Right: None
Node: 6, Left: None, Right: None

BFS Traversal:
1 2 3 4 7 5 6 ''' 
