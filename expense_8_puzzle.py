import copy 
import sys
import math
import copy
import random
popped = 0
expanded = 0
generated = 1
closed = []
max_fringe = 0
dump_flag = "false"
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

file_name = "trace-"+dt_string+""+".txt"

def write_to_file(data):
    global dump_flag
    global file_name
    if dump_flag == "false":
        return
    fh = open(file_name, "a")
    fh.write(data+"\n")
    fh.close()

def get_cost(data):
    cost = 0
    for line in data.split('\n')[1:]:
        cost += int(line.strip().split()[1])
    return cost

def generate_matrix(file):
    fh = open(file,'r')
    matrix = []
    for line in fh.readlines():
        row = []
        if line != "END OF FILE":
            for num in line.strip().split():
                row.append(int(num))
            matrix.append(row)
    #print(matrix)
    return matrix


def swap_ele(org_node, row1, col1, row2, col2):
    node = copy.deepcopy(org_node)
    cost = node[row2][col2]
    node[row1][col1] = cost
    node[row2][col2] = 0
    #print(cost)
    return node,  cost

def gen_content(state):
    if len(state) == 1:
        return str(state[0][0])
    return str(state[0])+"\n\tAction:"+str(state[2].split('\n')[-1])+", g(n):"+str(state[1])+", d:"+str(len(state[2].split('\n'))-1)+", f(n):"+str(get_cost(state[2]))

def generate_children(state):
    write_to_file("Generating successors to \nState:"+gen_content(state)+", \n\tParent:"+gen_content(state[5])+"\n"+"-"*48)
    node = state[0]
    global generated
    #print(node)
    nodes = []
    for r in range(0,3):
        for c in range(0,3):
            if node[r][c] == 0:
                #print(r)
                #print(c)
                row = r
                col = c
    
    if row == 0 and col == 0:
        new_node, node_cost = swap_ele(node, 0, 0, 0, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Left", node_cost])
        new_node, node_cost = swap_ele(node, 0, 0, 1, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Up", node_cost])
    elif row == 0 and col == 1:
        new_node, node_cost = swap_ele(node, 0, 1, 0, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Right", node_cost])
        new_node, node_cost = swap_ele(node, 0, 1, 0, 2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Left", node_cost])
        new_node, node_cost = swap_ele(node, 0, 1, 1, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Up", node_cost])
    elif row == 0 and col == 2:
        new_node, node_cost = swap_ele(node, 0, 2, 0, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Right", node_cost])
        new_node, node_cost = swap_ele(node, 0, 2, 1, 2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Up", node_cost])        
    elif row == 1 and col == 0:
        new_node, node_cost = swap_ele(node, 1, 0, 1, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Left", node_cost])
        new_node, node_cost = swap_ele(node, 1, 0, 0, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Down", node_cost])
        new_node, node_cost = swap_ele(node, 1, 0, 2, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Up", node_cost])
    elif row == 1 and col == 1:
        new_node, node_cost = swap_ele(node, 1, 1, 1, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Right", node_cost])
        new_node, node_cost = swap_ele(node, 1, 1, 1, 2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Left", node_cost])
        new_node, node_cost = swap_ele(node, 1, 1, 0, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Down", node_cost])
        new_node, node_cost = swap_ele(node, 1, 1, 2, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Up", node_cost])
    elif row == 1 and col == 2:
        new_node, node_cost = swap_ele(node, 1, 2, 1, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Right", node_cost])
        new_node, node_cost = swap_ele(node, 1, 2, 0 ,2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Down", node_cost])
        new_node, node_cost = swap_ele(node, 1, 2, 2, 2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Up", node_cost])
    elif row == 2 and col == 0:
        new_node, node_cost = swap_ele(node, 2, 0, 2, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Left", node_cost])
        new_node, node_cost = swap_ele(node, 2, 0, 1, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Down", node_cost])
    elif row == 2 and col == 1:
        new_node, node_cost = swap_ele(node, 2, 1, 2, 0)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Right", node_cost])
        new_node, node_cost = swap_ele(node, 2, 1, 2, 2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Left", node_cost])
        new_node, node_cost = swap_ele(node, 2, 1, 1, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Down", node_cost])
    elif row == 2 and col == 2:
        new_node, node_cost = swap_ele(node, 2, 2, 2, 1)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Right", node_cost])
        new_node, node_cost = swap_ele(node, 2, 2, 1, 2)
        nodes.append([new_node,  state[2]+"\n"+"Move "+str(node_cost)+" Down", node_cost])
    #print(nodes)
    generated += len(nodes)
    random.shuffle(nodes)
    write_to_file(str(len(nodes))+" successors generated"+"\n"+"-"*48)
    return nodes


def calculate_f(start_node, goal_node):
    #print(start_node)
    board = []
    for i in range(0,3):
        for val in start_node[i]:
            board.append(val)

    goal = []
    for i in range(0,3):
        for val in goal_node[i]:
            goal.append(val)

    sum = 0
    for i in range(1, 9):
        g_index = goal.index(i)
        b_index = board.index(i)
        col_c = abs(g_index%3 - b_index%3)
        row_c = abs(g_index//3 - b_index//3)
        sum += i * (row_c + col_c)
    return sum

def calculate_g(start_node, goal_node):
    #print(start_node)
    board = []
    for i in range(0,3):
        for val in start_node[i]:
            board.append(val)

    goal = []
    for i in range(0,3):
        for val in goal_node[i]:
            goal.append(val)

    sum = 0
    for i in range(1, 9):
        g_index = goal.index(i)
        b_index = board.index(i)
        col_c = abs(g_index%3 - b_index%3)
        row_c = abs(g_index//3 - b_index//3)
        sum += (row_c + col_c)
    return sum

def select_node(fringe, goal, method):
    global closed
    global popped
    popped += 1
    if method == "bfs":
        state = fringe.pop(0)
    elif method == "ucs":
        temp_fringe = sorted(fringe.copy(),key=lambda x: (x[4]))
        state = temp_fringe.pop(0)
        state_index = fringe.index(state)
        state = fringe.pop(state_index)
    elif method == "dfs":
        state = fringe.pop()
    elif method == "dls":
        state = fringe.pop()
    elif method == "ids":
        state = fringe.pop()
    elif method == "greedy":
        temp_fringe = sorted(fringe.copy(),key=lambda x: calculate_f(x[0], goal))
        state = temp_fringe.pop(0)
        state_index = fringe.index(state)
        state = fringe.pop(state_index)
    elif method == "a*":
        temp_fringe = sorted(fringe.copy(),key=lambda x: x[4] + calculate_f(x[0], goal))
        state = temp_fringe.pop(0)
        state_index = fringe.index(state)
        state = fringe.pop(state_index)
    return state, fringe

def search(st_state, goal, fringe, dump_flag, depth, method):
    global closed
    global expanded
    global max_fringe
    state, fringe = select_node(fringe, goal, method)
    closed.append(state[0])
    if method == "ids":
        original_state = state
        while True:
            while state[0] != goal :
                #print(state)
                #print("d:"+str(depth))
                
                expanded += 1
                children = generate_children(state)
                parent = [state[0],state[1],state[2],state[3],state[4],state[5][-1]]
                for child in children:
                    init_f = state[4] + child[2]
                    fringe.append([child[0], child[2], child[1], len(parent), init_f, parent])
                #print(len(fringe))
                if max_fringe < len(fringe):
                    max_fringe = len(fringe)
                while True:
                    if len(fringe) == 0:
                        break_flag = True
                        break
                    state, fringe = select_node(fringe, goal, method)
                    if state[0] in closed:
                        continue
                    else:
                        print(len(state[2].split('\n'))-1, depth)
                        if len(state[2].split('\n'))-1 > depth:
                            continue
                        closed.append(state[0])
                        break
                if break_flag:
                    break_flag = False
                    closed = []
                    break
            depth += 1
            if state[0] == goal:
                return state, fringe, closed
            state = original_state
            
    else:
        while state[0] != goal :
            expanded += 1
            children = generate_children(state)
            parent = [state[0],state[1],state[2],state[3],state[4],state[5][-1]]
            for child in children:
                init_f = state[4] + child[2]
                fringe.append([child[0], child[2], child[1], len(parent), init_f, parent])

            if max_fringe < len(fringe):
                max_fringe = len(fringe)

            while True:
                if len(fringe) == 0:
                    print("Goal not found!")
                    result()
                    exit()
                state, fringe = select_node(fringe, goal, method)
                if method != 'dls' and method != 'dfs':
                    if state[0] in closed:
                        continue
                    else:
                        closed.append(state[0])
                        break
                else: 
                    if method == "dls":
                        if len(state[2].split('\n'))-1 > depth:
                            continue
                        else:
                            break
                    
        return state, fringe, closed

def result():
    global popped
    global expanded
    global expanded
    global max_fringe
    write_to_file("\n\n")
    print("Nodes Popped: "+ str(popped))
    write_to_file("\t\tNodes Popped: "+ str(popped))
    print("Nodes Expanded: "+ str(expanded))
    write_to_file("\t\tNodes Expanded: "+ str(expanded))
    print("Nodes Generated: "+ str(generated))
    write_to_file("\t\tNodes Expanded: "+ str(generated))
    print("Max Fringe Size: "+ str(max_fringe))
    write_to_file("\t\tNodes Expanded: "+ str(max_fringe))

if __name__ =="__main__":
    if len(sys.argv) < 2:
        print("arg is missing")
        sys.exit()

    
    start_fl = sys.argv[1]
    goal_fl = sys.argv[2]
    if len(sys.argv) > 3:
        if len(sys.argv) == 4:
            if sys.argv[3].lower() == "true" or sys.argv[3].lower() =="false":
                dump_flag = sys.argv[3].lower()
                method = "a*"
            else:
                dump_flag = "false"
                method = sys.argv[3].lower()
        elif len(sys.argv) == 3:
            method = "a*"
            dump_flag = "false"
        else:
            dump_flag = sys.argv[4]
            method = sys.argv[3]
    #print("Command-Line Arguments : ['"+start_fl+"', '"+goal_fl+", '"+method+"', '"+dump_flag+"']")
    write_to_file("Command-Line Arguments : ['"+start_fl+"', '"+goal_fl+", '"+method+"', '"+dump_flag+"']")
       
    start_node = generate_matrix(start_fl)
    goal_node = generate_matrix(goal_fl)

    init_f = calculate_f(start_node, goal_node)
    fringe = []
    parent = [[["Pointer to None"]]]
    start = [start_node, 0, "Start", 0, init_f, parent]
    fringe.append(start)
    max_fringe = len(fringe)
    if method == "dls":
        depth = int(input("Enter the Depth:"))
    else:
        depth = 0
    write_to_file("Method Selected: "+method+"\nRunning "+method)
    state, fringe, closed = search(start, goal_node, fringe, dump_flag, depth, method)
    result()
    cost = 0
    for line in state[2].split('\n')[1:]:
        cost += int(line.strip().split()[1])
    print("Solution Found at depth "+str(len(state[2].split('\n'))-1)+" with cost of "+str(cost))
    print("Steps:")
    for line in state[2].split('\n')[1:]:
        print("    "+line)
    





