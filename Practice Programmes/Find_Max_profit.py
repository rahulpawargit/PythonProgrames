# prices = [10, 12, 9, 6, 8, 12]
# max_profit = 0
# min_profit = float('inf')
#
# for price in prices:
#     max_profit = max(max_profit, price - min_profit)
#     min_profit = min(min_profit, price)
#
# print(max_profit)

def find_max_profit(prices):
    max_profit = 0
    min_stock= float('inf')

    for price in prices:
        max_profit =max (max_profit, price - min_stock)
        min_stock =min(min_stock, price)
    return max_profit


prices = [10, 12, 9, 6, 8, 1,2]
print(find_max_profit(prices))

