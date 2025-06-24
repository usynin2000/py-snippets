# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.




def max_profit(prices: list) -> int:
    buy_price = prices[0]
    profit = 0

    for p in prices[1:]:
        if buy_price > p:
            buy_price = p

        profit = max(profit, p - buy_price)

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    print(max_profit(prices))

    prices = [7,6,4,3,1]

    print(max_profit(prices))