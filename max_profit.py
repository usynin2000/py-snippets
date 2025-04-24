


def max_profit_brute_force(prices: list[int]) -> int:
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]

            res = (max(res, sell - buy))

    return res


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_brute_force(prices))
