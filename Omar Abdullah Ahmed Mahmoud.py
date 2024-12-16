from itertools import permutations

# Input Data
conflicts = [
    {'sub_id': 100, 'Conflict_sub_id': 200, 'NumOfInteraction': 30},
    {'sub_id': 300, 'Conflict_sub_id': 100, 'NumOfInteraction': 15},
    {'sub_id': 300, 'Conflict_sub_id': 200, 'NumOfInteraction': 20},
]

levels = [
    {'sub_id': 100, 'level': 1},
    {'sub_id': 200, 'level': 2},
    {'sub_id': 300, 'level': 3},
]

# Define possible patterns
patterns = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

# Function to calculate the final cost for a given order
def calculate_cost(order, conflicts):
    cost = 0
    level_map = {sub['sub_id']: order.index(sub['level']) for sub in levels}
    
    for conflict in conflicts:
        sub1 = conflict['sub_id']
        sub2 = conflict['Conflict_sub_id']
        interaction = conflict['NumOfInteraction']
        
        # Add cost if there is an overlap in the same level
        if level_map[sub1] == level_map[sub2]:
            cost += interaction
    return cost

# Find the best order with minimum cost
def find_best_order():
    best_order = None
    min_cost = float('inf')

    for order in permutations([1, 2, 3]):  # Generate all possible arrangements
        cost = calculate_cost(order, conflicts)
        if cost < min_cost:
            min_cost = cost
            best_order = order

    return best_order, min_cost

# Execute the program
best_order, min_cost = find_best_order()
print("Best schedule order:", best_order)
print("Final cost (total overlaps):", min_cost)

# Omar Abdullah Ahmed Mahmoud
