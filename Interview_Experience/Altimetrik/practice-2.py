# How to update a tuple in a list of tuples?

# solution:

list_of_tuples = [(1, 2), (3, 4), (5, 6)]

# Find the index of the tuple you want to update.
index_of_tuple_to_update = 1

# Create a new tuple with the updated values.
new_tuple = (7, 8)

# Replace the old tuple with the new tuple in the list.
list_of_tuples[index_of_tuple_to_update] = new_tuple

print(list_of_tuples)