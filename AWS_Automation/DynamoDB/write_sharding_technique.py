# How To Fix Hot Partition

# Write Sharding Technique
# Add random prefix:

import random

shard = random.randint(0, 9)
partition_key = f"{shard}user#123"

print(f"Shard: {shard}")
print(f"Partition Key: {partition_key}")

