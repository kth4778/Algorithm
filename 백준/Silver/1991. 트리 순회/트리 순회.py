n = int(input())

tree = {}
for _ in range(n):
    root,left,right = input().split()
    tree[root] = [left,right]

def preorder(node,answer):
    if node == '.':
        return
    answer.append(node)
    preorder(tree[node][0],answer)
    preorder(tree[node][1],answer)

def inorder(node,answer):
    if node == '.':
        return
    inorder(tree[node][0],answer)
    answer.append(node)
    inorder(tree[node][1],answer)

def postorder(node,answer):
    if node == '.':
        return
    postorder(tree[node][0],answer)
    postorder(tree[node][1],answer)
    answer.append(node)



preorder_list = []
inorder_list = []
postorder_list = []

preorder('A',preorder_list)
inorder('A',inorder_list)
postorder('A',postorder_list)

print(''.join(preorder_list))
print(''.join(inorder_list))
print(''.join(postorder_list))