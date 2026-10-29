class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = float('inf')
        max_sell_price = float('-inf')

        max_profit = float('-inf')

        for p in prices:
            # print("MIN BUY (BEFORE): ", min_buy_price)
            # print("MAX SELL (BEFORE): ",max_sell_price)
            # print("PROFIT (BEFORE): ", max_profit)
            if p < min_buy_price:
                min_buy_price = p
                max_sell_price = float('-inf')
                continue
            
            if p > max_sell_price:
                max_sell_price = p
                max_profit = max(max_sell_price - min_buy_price, max_profit)

            # print("MIN BUY (AFTER): ", min_buy_price)
            # print("MAX SELL (AFTER): ",max_sell_price)
            # print("PROFIT (AFTER): ", max_profit)
            # print('\n')

        return max(0, max_profit)