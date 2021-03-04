from datetime import datetime
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
# print("MetaTrader5 package author: ", mt5.__author__)
# print("MetaTrader5 package version: ", mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd

if not mt5.initialize(login=42094961, server="MetaQuotes-Demo",password="bvboq4lt"):
    print("initialize() failed, error code =", mt5.last_error())
    quit()


pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display

final_list = []

# get all symbols
symbols = mt5.symbols_get()
# print('Symbols: ', len(symbols))
count = 0
# display the first five ones
for s in symbols:
    count += 1
    # print("{}. {}".format(count, s.name))


    # if s.name[:3] == "USD":
        # get 10 GBPUSD D1 bars from the current day
    rates = mt5.copy_rates_from_pos(s.name, mt5.TIMEFRAME_D1,0,1)
    if rates:

        # for rate in rates:
        change = ((float(rates[0][4]) - float(rates[0][1]))/float(rates[0][1]))*100
        change = round(change, 2)
        change_str = "{}%".format(change)
        # print(change_str)
        sell = round(rates[0][1], 5)
        low = round(rates[0][3], 5)
        high = round(rates[0][2], 5)
        buy = round(rates[0][4], 5)

        info = [s.name, low, high, change_str, sell, buy]
        final_list.append(info)
        # print(info)

        change = 0
        change_str = ""
        info = ""
        sell = ""
        buy = ""
        low = ""
        high = ""

        if count == 102: break

    else:
        info = [s.name, "-", "-", "-", "-", "-"]
        final_list.append(info)


# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# for i in final_list:
#     print(i)

