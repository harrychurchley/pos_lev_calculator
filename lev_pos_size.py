# this is a leverage and position size calculator

# import dependencies

import pandas as pd
from binance import client, 

account_size = 1000
risk_pc = 2
risk_raw = account_size*(risk_pc/100)




def place_trade(coin, buy_price, take_profit, stop_loss):
    invalidation = ((buy_price - stop_loss)/buy_price) * 100
    leverage = risk_pc/invalidation
    position_size = account_size * leverage
    return print(leverage, position_size)

place_trade('BTC', 4000, 4500, 3500)