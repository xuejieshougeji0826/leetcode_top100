# 如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元



__author__ = 'ice'


def select_coin(coin_value, total_value):
    min_coin_num = [0]
    for i in range(1, total_value + 1):
        min_coin_num.append(float('inf'))
        print(min_coin_num)
        for value in coin_value:
            if value <= i and min_coin_num[i - value] + 1 < min_coin_num[i]:
                min_coin_num[i] = min_coin_num[i - value] + 1
                print(min_coin_num)

    return min_coin_num

class Solution:
    def coinChange(self, coins,amount ) :
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    print('i:', i, 'coin:',coin)
                    print('xuanze:',dp[i], dp[i - coin] + 1)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    print(dp)
        # print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1
# result = select_coin([1, 3, 5], 11)
# print("coin number:" + str(result[-1]))
s=Solution()
print(s.coinChange([1,3,5],11))