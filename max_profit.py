def max_profit_brute_force(prices: list[int]) -> int:
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]

            res = max(res, sell - buy)

    return res


def max_profit_l_r(prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_brute_force(prices))
    print(max_profit_l_r(prices))
