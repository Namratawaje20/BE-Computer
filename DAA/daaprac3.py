class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            total_value += item.ratio * capacity
            capacity = 0

    return total_value

# Example usage
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
max_value = fractional_knapsack(capacity, items)
print("Maximum value in Knapsack =", max_value)
