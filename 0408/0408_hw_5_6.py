root_node = 0
tree = [[1,2,3],[4],[8,9,10],[5],[6,7],[],[],[],[],[],[]]
values = ['030','054','002','045','001','123','456','789','888','999','000']

def preorder(node, step):
    if len(tree[node]) == 0: print();return;
    
    for i in range(len(tree[node])):
        if len(tree[node]) == 1:
            print('-----', '[%s]' %values[tree[node][i]], end='')
        else:
            if i == len(tree[node]) - 1:
                print('      '*step + '     '*(step-1),'L--', '[%s]' %values[tree[node][i]], end = '')
            elif i == 0:
                print('--', end='')
                print('+--',  '[%s]' %values[tree[node][i]], end = '')
            else:
                print('      '*step + '     '*(step-1),'+--',  '[%s]' %values[tree[node][i]], end = '')
        preorder(tree[node][i], step+1)

print('[%s]' %values[root_node], end='')
preorder(root_node, 1)