#Note same code as problem 18 with different binary tree file

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
    first_line = tree[0]
    second_line = tree[1]
    for j in range( len(second_line) ):
        second_line[j] = max( first_line[j]+second_line[j], first_line[j+1]+second_line[j] )
    tree[1] = second_line
    tree.remove(tree[0])
    number_of_lines = len(tree)

print(tree[0][0])