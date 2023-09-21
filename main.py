# from fibo import fib, fib2
# import googleSignIn
# googleSignIn.googleSignInFunction("Jonathan")

from google_signIn import google__sign__function
import schedule
import time
from zerodha_sell_positions import zerodha__sell__positions
from sets_quantity_price import minutes__run__sell__time

def main():
    # 1. Sign into Google Account  (include check if account exists or not)
    google__sign__function()

    # 2. Switch to new tab 
    # provided in google_signIn.

    # 3. open trading view screener in new switched tab
    # provided in google_signIn

    # 4. Sign in with google account in trading view (include check if account exists or not)
    # in trading_view_sign in.py

    # 5. redirect to screener
    # in trading_view_sign in.py

    # 6. on screener we have filter()
    # in trading_view_screener.py     

    # 7. select the right filter
    # trading_view_filter.py

    # 8. Select and store value from filter
    # trading_view_filter.py
    # select_value_from_filter.py 

    # 9. access stocks in zerodha from select_value_from filter
    # zerodha_access_filter_value.py

    # 10. add filtered stocks to zerodha 
    # zerodha_access_filter_value.py
    # zerodha_add_filtered_stocks.py

    # 11. placed the buy orders for all filtered stocks
    # zerodha_add_filtered_stocks.py
    # zerodha_buy_orders.py     

    # 12. placed the sell orders for positions
    # zerodha_add_filtered_stocks.py
    # zerodha_sell_positions.py
    # main.py

    zerodha__sell__positions()
    
if __name__=="__main__":
    main()

    # set up sell running or every 1 min
    schedule.every(minutes__run__sell__time).minutes.do(zerodha__sell__positions)

    while True:
        schedule.run_pending()
        time.sleep(1)
