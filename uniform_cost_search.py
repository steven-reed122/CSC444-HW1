import heapq


# uniform cost function
# returns the minimum cost and the path with minimum cost

def uniform_cost_search(start, goal, graph, cost):
    answer = {node: {'cost': float('inf'), 'path': []} for node in goal}

    # priority queue for fringe (min-heap)
    pq = []
    heapq.heappush(pq, (0, start, [start]))  # (cost, node, path)

    # dictionary to store the minimum cost to reach each node and the corresponding path
    min_cost_dict = {}

    # explore the graph until the pq is empty
    # aka all paths have been explored
    while pq:
        current_cost, current_node, path = heapq.heappop(pq)

        # if the node has already been visited with a lower cost, skip
        if current_node in min_cost_dict and min_cost_dict[current_node]['cost'] <= current_cost:
            continue

        # store the cost and path
        min_cost_dict[current_node] = {'cost': current_cost, 'path': path}

        # if we reach the goal state, update answer
        if current_node in goal:
            answer[current_node] = {'cost': current_cost, 'path': path}
            continue

        # explore neighbors of current node
        for neighbor in graph[current_node]:
            # find total-cost to get to neighbor
            edge_cost = cost.get((current_node, neighbor), float('inf'))
            total_cost = current_cost + edge_cost
            # add neighbors to the prio-q
            heapq.heappush(pq, (total_cost, neighbor, path + [neighbor]))

    return answer


# another test graph
def test_graph_1():
    #create a graph with no more than 30 nodes
    graph1, cost1 = [[] for i in range(30)], {}

    #add edges to graph
    graph1[0].append(1)
    graph1[1].append(2)
    graph1[2].append(3)
    graph1[2].append(5)
    graph1[2].append(8)
    graph1[3].append(4)
    graph1[3].append(5)
    graph1[5].append(5)
    graph1[5].append(6)
    graph1[6].append(7)
    graph1[6].append(8)
    graph1[7].append(8)

    #add cost to each edge
    cost1[(0,1)] = 4
    cost1[(1,2)] = 8
    cost1[(2,3)] = 7
    cost1[(2,5)] = 4
    cost1[(2,8)] = 2
    cost1[(3,4)] = 9
    cost1[(3,5)] = 14
    cost1[(4,5)] = 10
    cost1[(5,6)] = 2
    cost1[(6,7)] = 1
    cost1[(6,8)] = 6
    cost1[(7,8)] = 7

    # set start state
    start1 = 0

    # set goal state, there can be multiple goal states
    goal1 = [7]

    return graph1, cost1, start1, goal1

def test_graph_2():
    # create a graph with no more than 30 nodes
    graph2, cost2 = [[] for i in range(30)], {}

    #add edges to graph
    graph2[1].append(2)
    graph2[1].append(3)
    graph2[2].append(1)
    graph2[2].append(4)
    graph2[3].append(4)
    graph2[4].append(8)
    graph2[5].append(4)
    graph2[5].append(6)
    graph2[5].append(7)
    graph2[5].append(8)
    graph2[6].append(7)
    graph2[7].append(5)
    graph2[7].append(8)
    graph2[8].append(5)

    #add costs to edges
    cost2[(1, 2)] = 9
    cost2[(1, 3)] = 5
    cost2[(2, 1)] = 3
    cost2[(2, 4)] = 18
    cost2[(3, 4)] = 12
    cost2[(4, 8)] = 8
    cost2[(5, 4)] = 9
    cost2[(5, 6)] = 2
    cost2[(5, 7)] = 5
    cost2[(5, 8)] = 3
    cost2[(6, 7)] = 1
    cost2[(7, 5)] = 4
    cost2[(7, 8)] = 6
    cost2[(8, 5)] = 3

    start2 = 1
    goal2 = [7]

    return graph2, cost2, start2, goal2

# main function
if __name__ == '__main__':

    # create a graph with no more than 30 nodes
    graph, cost = [[] for i in range(30)], {}

    # add edges to the graph
    graph[0].append(4)
    graph[0].append(5)
    graph[0].append(16)
    graph[2].append(1)
    graph[3].append(1)
    graph[4].append(2)
    graph[4].append(3)
    graph[4].append(5)
    graph[5].append(8)
    graph[5].append(18)
    graph[6].append(3)
    graph[6].append(7)
    graph[8].append(16)
    graph[8].append(17)
    graph[16].append(17)
    graph[18].append(6)

    # add cost to each edge
    cost[(0, 4)] = 3
    cost[(0, 5)] = 9
    cost[(0, 16)] = 1
    cost[(2, 1)] = 2
    cost[(3, 1)] = 2
    cost[(4, 2)] = 1
    cost[(4, 3)] = 8
    cost[(4, 5)] = 2
    cost[(5, 8)] = 3
    cost[(5, 18)] = 2
    cost[(6, 3)] = 3
    cost[(6, 7)] = 2
    cost[(8, 16)] = 4
    cost[(8, 17)] = 4
    cost[(16, 17)] = 15
    cost[(18, 6)] = 1

    # set start state
    start = 0

    # set goal state, there can be multiple goal states
    goal = [7]

    # call uniform_search_cost function to get the minimum cost to reach the goal and the path with minumum cost
    # ****** You have to implement this function *****
    min_cost_info = uniform_cost_search(start, goal, graph, cost)

    for node, info in min_cost_info.items():
        print(f'Minimum cost from {start} to {node} is {info["cost"]}')
        print(f'Path: {info["path"]}')

    graph, cost, start, goal = test_graph_1()
    min_cost_info = uniform_cost_search(start, goal, graph, cost)

    for node, info in min_cost_info.items():
        print(f'Minimum cost from {start} to {node} is {info["cost"]}')
        print(f'Path: {info["path"]}')

    graph, cost, start, goal = test_graph_2()
    min_cost_info = uniform_cost_search(start, goal, graph, cost)
    for node, info in min_cost_info.items():
        print(f'Minimum cost from {start} to {node} is {info["cost"]}')
        print(f'Path: {info["path"]}')

