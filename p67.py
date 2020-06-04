#Note almost the same code as problem 18 with different binary tree file abd less memory used

with open("p67_binary_tree.txt", "r") as f:
    tree = []
    for line in f:
        nodes = []
        node_string = line.split()
        for node in node_string:
            nodes.append(int(node))
        tree.append(nodes)

tree.reverse()
number_of_lines = len(tree)

while number_of_lines > 1:
    for j in range( len(tree[1]) ):
        tree[1][j] = max( tree[0][j]+tree[1][j], tree[0][j+1]+tree[1][j] )
    tree.remove(tree[0])
    number_of_lines = len(tree)

print(tree[0][0])