class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        for i in range(len(gas)):
            begin=[]
            if gas[i]>=cost[i]:
                begin.append(i)
        print(begin)
s = Solution()
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print(s.canCompleteCircuit(gas,cost))
