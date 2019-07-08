from random import randint


with open('test.txt') as file:
    mincut_data = []
    for line in file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            mincut_data.append(line)


edge_list = []
node_list = []
for every_list in mincut_data:
    node_list.append(every_list[0])
    temp_list = []
    for temp in range(1, len(every_list)):
        temp_list = [every_list[0], every_list[temp]]
        flag = 0
        for j in edge_list:
            if set(j) == set(temp_list):
                flag = 1
        if flag == 0:
            edge_list.append([every_list[0], every_list[temp]])


while len(node_list) > 2:
    res = randint(0, (len(edge_list)-1))
    print(res)
    edge = edge_list[res]
    replace = edge[0]
    replace2 = edge[1]
    for edge in edge_list:
        if edge[0] == replace2:
            edge[0] = replace
        if edge[1] == replace2:
            edge[1] = replace
    edge_list.remove(edge)
    node_list.remove(replace2)
    for edge in edge_list:
        if edge[0] == edge[1]:
            edge_list.remove(edge)
print("edge", edge_list)
print("node", node_list)