#!/usr/bin/python
# -*- coding: UTF-8 -*-
money = int(input('请输入利润总数：'))
if  money <= 100000:
    print("01应发放的奖金总数为：%d " % float(money*0.1))
elif money > 100000 and money < 200000:
    print("02应发放的奖金总数为：%d " % (float(100000*0.1) + float(money-100000)*0.075))
elif money > 200000 and money < 400000:
    print("03应发放的奖金总数为：%d " % (float(100000 * 0.1) + float(money - 100000) * 0.075 + float(money - 200000) * 0.05))
elif money > 400000 and money < 600000:
    print("04应发放的奖金总数为：%d " % (float(100000 * 0.1) + float(money - 100000) * 0.075 + float(money - 200000) * 0.05 + float(money - 400000)*0.03))
elif money > 400000 and money < 600000:
    print( "05应发放的奖金总数为：%d " % (float(100000 * 0.1) + float(money - 100000) * 0.075 + float(money - 200000) * 0.05 + float(money - 400000) * 0.03))
elif money > 600000 and money < 1000000:
    print( "06应发放的奖金总数为：%d " % (float(100000 * 0.1) + float(money - 100000) * 0.075 + float(money - 200000) * 0.05 + float(money - 400000) * 0.03 + float(money - 600000) * 0.015))
elif money > 1000000:
    print( "07应发放的奖金总数为：%d " % (float(100000 * 0.1) + float(money - 100000) * 0.075 + float(money - 200000) * 0.05 + float( money - 400000) * 0.03 + float(money - 600000) * 0.015 +float(money - 1000000) * 0.01))
else:
    pass
