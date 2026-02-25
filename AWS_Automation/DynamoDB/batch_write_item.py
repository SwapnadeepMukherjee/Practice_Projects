# Use BatchWriteItem:

# Instead of many single writes:
# Use batch writes:

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
