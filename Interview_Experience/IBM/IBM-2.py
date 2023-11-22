# adding items to a cart -

value = 0
cart_value = 0


def sumcart(items, cart_value=0):
    for i in range(len(items)):
        # print(items[i])
        value = items[i][1] * items[i][2]
        # print(value)
        #     for j in items[i]:
        #         value = j[1] * j[2]
        cart_value = cart_value + value
        # print(cart_value)
    #
    return cart_value


print(sumcart(items=[['item-1', 10, 20], ['item-2', 30, 40]]))
