class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in range(len(costs)):
            if costs[i]<=coins:
                coins=coins-costs[i]
                c+=1
            elif costs[i]>coins:
                break
        return c



        