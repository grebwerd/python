class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        retval = 0
        ownedStockPrice = 0
        ownStock = False
        counter = 0
        while counter < len(prices):
            if counter < len(prices)-1:
                if (prices[counter] < prices[counter+1]) and ownStock is False:
                    ownStock = True
                    ownedStockPrice = prices[counter]
                elif(ownedStockPrice < prices[counter]) and ownStock is True:
                    if prices[counter] - ownedStockPrice > prices[counter+1] - ownedStockPrice:
                        retval += prices[counter] - ownedStockPrice
                        ownStock = False
            if counter == len(prices) - 1 and ownStock is True:
                retval += prices[counter] - ownedStockPrice
            counter += 1
        return retval
