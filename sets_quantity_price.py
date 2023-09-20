
#------------for Buy (zerodha_buy_orders.py)--------------#

#sets no of quantities for buy
quantity__for__buy = 2
#sets the how much mius price u want from current/last traded price
price__for__buy = [1, 3, 5] 

#------------for sell (zerodha_sell_positions.py)--------------#

#sets no of quantities for sell
quantity__for__sell = 1
#sets the how much + price u want from current/last traded price
price__for__sell = 1

#-----------------for filter id (trading_view_filter.py)-----------------------#

# data-set="4486592" - S - TOP LOSERS
# data-set="4437803" - B - TOP GAINERS
# data-set="4437799" - B - VWAP CROSS SMA50
# data-set="4175380" - S - VERY RISKY - INTRADAY
# data-set="4175374" - B - VERY RISKY - INTRADAY
# data-set="4175365" - B - UPTREND
# data-set="4175361" - DIVIDEND STOCKS
# data-set="4175349" - L B - BOUNCEPLAY - VERY RISKY
# data-set="4175338" - S - HOLD - RISKY
# data-set="4175325" - B - Breakouts Stocks
# data-set="4175301" - L B - BOUNCEBACK (RISK HIGH)
# data-set="4175281" - B - LONG TERM HOLD
# data-set="4175264" - S - GAP DOWN STOCKS
# data-set="4175244" - B - GAP UP STOCKS
# data-set="4175228" - B - 50 MA CROSS ABV 200MA
# data-set="4174707" - B - INTRADAY - (- ve 3)

filter__id = 4174707


#-----------------for select no of stocks from filter (select_value_from_filter.py)--------------------

select__numbers__of__stocks = 2