class Solution(object):
    
    def maxProfit(self, prices):
        
        """
        :type prices: List[int]
        :rtype: int
        """
        
        rows = len(prices)
        cols = len(prices)
        lst = []
        
        for row in range(rows):
          for col in range(cols):
              if (col > row) and (prices[col] > prices[row]):
                  sell_day, buy_day, profit = col, row, prices[col] - prices[row]
                  lst.append((sell_day, buy_day, profit))
        
        # print (lst)
        x = sorted(lst, key=lambda transaction: transaction[1])
        # print ("sorted in profit order")
        # print (x)
        
        lst2 = []
        profit_list = []

        if (len(x) == 0):
            profit = 0
        else:    
            for i, item1 in enumerate(x):
                lst1 = []
                lst1.append(item1) 
                tup = item1
                for j, item2 in enumerate(x):
                  if (tup != item2 and item2[1] > tup[0]):
                      lst1.append(item2)
                      tup = item2 #save most recent transaction
                      lst2.append(lst1)
                  else:
                      lst2.append(lst1)
                # lst2.append(lst1)  

            # print (lst2)
            profit_list = []
            for transactions in lst2:
                profit = 0
                for one_transaction in transactions:
                    profit += one_transaction[2]
                profit_list.append(profit)
            # print (profit_list)
            profit = max(profit_list)
        
        return profit    
    

# prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [6,1,3,2,4,7]
prices = [3,3,5,0,0,3,1,4]
profit = Solution().maxProfit(prices)
print (profit)
        
