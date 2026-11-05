def max_crossing(diffs, low, mid, high):
    """Best subarray that crosses the midpoint."""
    left_sum = float("-inf")
    total = 0
    best_left = mid
    for i in range(mid, low - 1, -1):
        total += diffs[i]
        if total > left_sum:
            left_sum = total
            best_left = i

    right_sum = float("-inf")
    total = 0
    best_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += diffs[j]
        if total > right_sum:
            right_sum = total
            best_right = j

    return best_left, best_right, left_sum + right_sum


def max_subarray(diffs, low, high):
    """Divide and Conquer: returns (start, end, max_sum)."""
    if low == high:  # base case: a single day
        return low, high, diffs[low]

    mid = (low + high) // 2
    left = max_subarray(diffs, low, mid)
    right = max_subarray(diffs, mid + 1, high)
    cross = max_crossing(diffs, low, mid, high)

    return max(left, right, cross, key=lambda x: x[2])


def max_profit(prices):
    """Returns (buy_day, sell_day, profit)."""
    diffs = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    start, end, profit = max_subarray(diffs, 0, len(diffs) - 1)
    return start, end + 1, profit


def linear_scan(prices):
    """Simple O(n) solution, used for comparison."""
    min_price, min_day = prices[0], 0
    best = (0, 0, 0)
    for day, price in enumerate(prices):
        if price - min_price > best[2]:
            best = (min_day, day, price - min_price)
        if price < min_price:
            min_price, min_day = price, day
    return best


if __name__ == "__main__":
    prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

    buy, sell, profit = max_profit(prices)
    print("Divide and Conquer:")
    print(f"  Buy on day {buy} (price {prices[buy]})")
    print(f"  Sell on day {sell} (price {prices[sell]})")
    print(f"  Profit = {profit}")

    buy2, sell2, profit2 = linear_scan(prices)
    print("\nLinear Scan:")
    print(f"  Buy on day {buy2}, sell on day {sell2}, profit = {profit2}")
