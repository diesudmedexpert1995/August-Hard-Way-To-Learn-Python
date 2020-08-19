def find_lowest_cost(cost):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in cost:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node


costs = {}
graph = {}
parents = {}
processed = []

node = find_lowest_cost(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost(costs)
