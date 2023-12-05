def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

# Example usage:
my_list = [1, 2, 3, 4, 5]
index = 2
result = element_at(my_list, index)
print("Element at index {}: {}".format(index, result))
