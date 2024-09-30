'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''
def buySellStock(prices):

    '''
    Compares current stock price with previous price and adds in case of a profit
    Time Complexity: O(n) where n is number of items in prices
    Space Complexity: O(1)
    '''
    profit = 0
    l = len(prices)
    if l == 1:
        return profit

    for i in range(1, l):
        if prices[i] > prices[i-1]:
            profit = profit + (prices[i] - prices[i-1])
    return profit

print("Profit is :", buySellStock([1,2,3,4,5]))
print("Profit is :", buySellStock([7,6,4,3,1]))