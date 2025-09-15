# Problem 1:

# A company is planning a big sale at which they will give their customers a special promotional discount. each customer that purchases the product from the company has a unique customerid numbered from 0 to n-1. Andy, the marketing head of the company, has selected the bill amounts of the n customers for the promotional scheme. the discount will be given to the customers whose bill amounts are perfect squares. The customer may use this discount on a future purchase. 

# Write an algorithm to help andy find the number of customers that will be given discounts in python3 code:

import math

def count_perfect_square_discounts(bill_amounts):
    """
    Counts the number of perfect squares in a list of bill amounts.

    Args:
        bill_amounts: A list of integers representing the bill amounts.

    Returns:
        An integer representing the number of customers who will receive a discount.
    """
    discount_count = 0
    for amount in bill_amounts:
        if amount >= 0:
            square_root = int(math.sqrt(amount))
            if square_root * square_root == amount:
                discount_count += 1
    return discount_count

# Example Usage:
# n = 5
# bill_amounts = [100, 49, 12, 81, 250]
# discounts = count_perfect_square_discounts(bill_amounts)
# print(f"Number of customers receiving a discount: {discounts}")


