# Practice_Problem - 1 -
#
# Instruction
# To be completed in 10 min
# Implement a group_by_owners function that: Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

# 1. Solution Approach - Less Efficient/Nasty Approach(To be not taken just for clarification purpose) -

# Start-up code -

def group_by_owners(files):
    print(files.keys())
    print(files.values())
    print(dir(files))

    dict = {}
    for owner_temp in files.values():
        print("Current Owner:", owner_temp)
        owned = []
        for key_temp in files.keys():
            print(files[key_temp], files[key_temp] == "Randy", files[key_temp] == owner_temp)
            if files[key_temp] == owner_temp:
                owned.append(key_temp)
            print("results", owner_temp, owned)
            dict[owner_temp] = owned
    return dict


# Driver Code -
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

# print(group_by_owners(files))

# 2. Solution Approach - Efficient/Elegant solution -

from collections import defaultdict


def group_by_owners(files):
    owners = defaultdict(list)
    for owned, owner in files.items():
        print(owned, owner)
        owners[owned].append(owned)

    return dict(owners)


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
