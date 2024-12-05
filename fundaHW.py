def cost(money):
    cost={ 20:0, 10:0, 5:0, 2:0, 1:0 }
    for coin in cost:
        while money >=coin:
            money -= coin
            cost[coin] +=1
    return cost.items()

money=int(input("pls enter cost"))
change=cost(money)
for coin, money in change:
    print(f"{coin} bath-{money} coin")



