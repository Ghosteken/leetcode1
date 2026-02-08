from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') 
        max_profit = 0       
            
        for price in prices:
            if price < min_price:
                min_price = price
                
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    
    
    
    
    from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

