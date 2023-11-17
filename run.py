import pandas as pd
import numpy as np
import yfinance as yf
import requests
import time
import json

from datetime import datetime, timedelta


prev_day = '2023-11-16'
prev_next_day = '2023-11-17'

today = '2023-11-17'
tomorrow = '2023-11-18'

# symbols = ['RTNINDIA.NS','GEOJITFSL.NS','BHEL.NS']

symbols = [
    "MAHABANK.NS",
    "CENTRALBK.NS",
    "ORIENTPPR.NS",
    "COFFEEDAY.NS",
    # "PATELENG.NS",
    "RENUKA.NS",
    "NHPC.NS",
    # "UTKARSHBNK.NS",
    "DEN.NS",
    # "RADHIKAJWE.NS",
    "GOLDBEES.NS",
    "MMTC.NS",
    "UJJIVANSFB.NS",
    "DCW.NS",
    "PSUBNKBEES.NS",
    "GMRINFRA.NS",
    "RTNINDIA.NS",
    "MSUMI.NS",
    "EDELWEISS.NS",
    "IDBI.NS",
    "PARADEEP.NS",
    "GEOJITFSL.NS",
    "HFCL.NS",
    "NBCC.NS",
    "NFL.NS",
    "SILVERBEES.NS",
    "NETWORK18.NS",
    "IRFC.NS",
    "TRU.NS",
    "SJVN.NS",
    "PNB.NS",
    "HUDCO.NS",
    "IBREALEST.NS",
    "ALEMBICLTD.NS",
    # "VASCONEQ.NS",
    "ASIANTILES.NS",
    "IDFCFIRSTB.NS",
    "PNBGILTS.NS",
    "SAIL.NS",
    "CESC.NS",
    "TTML.NS",
    "JMFINANCIL.NS",
    "ELECTCAST.NS",
    "DWARKESH.NS",
    "MOTHERSON.NS",
    "NATIONALUM.NS",
    # "APOLLO.NS",
    "IOC.NS",
    "EQUITASBNK.NS",
    "BANKINDIA.NS",
    "SEQUENT.NS",
    "SHRIRAMPPS.NS",
    "HITECH.NS",
    "UNIONBANK.NS",
    "PPLPHARMA.NS",
    "J&KBANK.NS",
    "IIFLSEC.NS",
    "LEMONTREE.NS",
]

i=4

users = dict(pd.read_json('users.json', typ='series'))
trade_data = users['TRADE_DATA']

prev_sample = yf.download( symbols , start=prev_day , end=prev_next_day , interval='5m' )

market_time=['09:15', '09:20', '09:25', '09:30', '09:35', '09:40', '09:45', '09:50', '09:55', '10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55', '11:00', '11:05', '11:10', '11:15', '11:20', '11:25', '11:30', '11:35', '11:40', '11:45', '11:50', '11:55', '12:00', '12:05', '12:10', '12:15', '12:20', '12:25', '12:30', '12:35', '12:40', '12:45', '12:50', '12:55', '13:00', '13:05', '13:10', '13:15', '13:20', '13:25', '13:30', '13:35', '13:40', '13:45', '13:50', '13:55', '14:00', '14:05', '14:10', '14:15', '14:20', '14:25', '14:30', '14:35', '14:40', '14:45', '14:50', '14:55', '15:00', '15:05', '15:10', '15:15', '15:20', '15:25']

market_status = "CLOSED"

# while True:
#     current_time = datetime.now()
#     print("Time now : :",current_time)
#     # if current_time.second == 57 :
#     sample = yf.download( 'BHEL.NS' , start=prev_day , end=prev_next_day )
#     C = list(sample['Close'])
#     print(C[-1])
#     time.sleep(1)

# trade_data = dict([("TRADE", ''), ("TRADE_SYMBOL", ''), ("POS", ''), ("SELL_PRICE", ''), ("SELL_TIME", ''), ("BUY_PRICE", ''), ("BUY_TIME", ''), ("QTY", 1), ("PNL", '') ])
# trade_data['USER']='SVM041'
# saveCandleToJsonFile('tradeHistory/'+tomorrow,trade_data)

# def placeMisSellOrder(symbol,qty):
#     try:
#         order_id = kite.place_order(tradingsymbol=symbol,
#                                     exchange=kite.EXCHANGE_NSE,
#                                     transaction_type=kite.TRANSACTION_TYPE_SELL,
#                                     quantity=qty,
#                                     variety=kite.VARIETY_REGULAR,
#                                     order_type=kite.ORDER_TYPE_MARKET,
#                                     product=kite.PRODUCT_MIS,
#                                     validity=kite.VALIDITY_IOC)

#         logging.info("Order placed. ID is: {}".format(order_id))
#     except Exception as e:
#         logging.info("Order placement failed: {}".format(e.message))
#     return order_id

# def placeMisBuyOrder(symbol,qty):
#     try:
#         order_id = kite.place_order(tradingsymbol=symbol,
#                                     exchange=kite.EXCHANGE_NSE,
#                                     transaction_type=kite.TRANSACTION_TYPE_BUY,
#                                     quantity=qty,
#                                     variety=kite.VARIETY_REGULAR,
#                                     order_type=kite.ORDER_TYPE_MARKET,
#                                     product=kite.PRODUCT_MIS,
#                                     validity=kite.VALIDITY_IOC)

#         logging.info("Order placed. ID is: {}".format(order_id))
#     except Exception as e:
#         logging.info("Order placement failed: {}".format(e.message))
#     return order_id

# def getActivePosition(ticker):
#     position = kite.positions()
#     day_position = position['day']
#     active_position = [x for x in day_position if x['quantity'] != 0]
#     position = active_position[ticker]
#     return position


    
def saveCandleToJsonFile( filename, data ):
    jsonString = json.dumps(data)
    with open(filename+".json", "w") as outfile:
        outfile.write(jsonString)

def saveUserToHistory():
    users = dict(pd.read_json('users.json', typ='series'))
    history = dict(users['TRADE_DATA'])
    history['USER']='SVM041'
    saveCandleToJsonFile('tradeHistory/'+today,history)

def resetUser():
    saveCandleToJsonFile('users',{
    "TRADE_DATA": {
        "TRADE": "",
        "TRADE_SYMBOL": "",
        "POS": "EXIT",
        "SELL_PRICE": "",
        "SELL_TIME": "",
        "BUY_PRICE": "",
        "BUY_TIME": "",
        "QTY": 1,
        "PNL": ""
    },
    "USER": "SVM041",
    "SVM041": { "API_KEY": "", "API_SECRET": "", "ACCESS_TOCKEN": "" }
    })

def tryToGetTarget():
    while True:
        current_time = datetime.now()
        if current_time.strftime("%Y-%m-%d") != today:
            print('Pls change today value to current date')
            break
        users = dict(pd.read_json('users.json', typ='series'))
        trade_data = users['TRADE_DATA']
        
        if ( ( current_time.minute % 5 ) == 0  ) and ( current_time.second == 00 ):
            time.sleep(2)

        if( trade_data['POS']=='SELL'):

            sample = yf.download( trade_data['TRADE_SYMBOL'] , start=today , end=tomorrow )

            C = list(sample['Close'])
            if (not (trade_data['SELL_PRICE'] is None)) and ( len( C ) > 0 ) and ( ( trade_data['SELL_PRICE'] - 0.7 ) > C[-1] ):
                        print(current_time.strftime("%Y-%m-%d %H:%M:%S"),'Buy Order',trade_data['TRADE_SYMBOL'])
        #               place buy order wait for conformation buy checking postion from kite 
                        # time.sleep(5)
                        # after 5 second get position status of order and pls conform trade exit position
                        # print(market_time[i],'Get Position',ticker)
        #               if true
                        trade_data['POS'] = 'EXIT'
                        # print("Price",sample['Close'][-1])
                        trade_data['BUY_PRICE'] = C[-1] # this should be from buy order response
                        trade_data['BUY_TIME'] = current_time.strftime("%Y-%m-%d %H:%M:%S")
                        trade_data['PNL'] = ( trade_data['SELL_PRICE'] - trade_data['BUY_PRICE'] ) * trade_data['QTY']  # this should be from buy position response
                        users['TRADE_DATA'] = dict(trade_data)
                        
                        saveCandleToJsonFile('users',users)
                        saveUserToHistory()
                        # history = pd.read_json('tradeHistory.json', typ='series')
                        # history[today] = users
                        # saveCandleToJsonFile('tradeHistory',history)
                        # print(market_time[i],ticker,'Exit Position')
                        break
        #               place order is failed then try until sucesss
        time.sleep(1)
        

if ( trade_data['POS'] == 'SELL' and trade_data['TRADE'] == 'OK' ):
    tryToGetTarget()


while True:
    current_time = datetime.now()
    if current_time.strftime("%Y-%m-%d") != today:
        print('Pls change today value to current date')
        break
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    # 9, 34, 59)
    market_open_time = datetime(year, month, day, 9, 35, 00)
    market_intermediate_time = datetime(year, month, day, 14, 35, 00)
    market_close_time = datetime(year, month, day, 15, 15, 00)

    users = dict(pd.read_json('users.json', typ='series'))
    trade_data = dict(users['TRADE_DATA'])

    if ( market_open_time < current_time ) and  ( market_intermediate_time > current_time ):
        market_status = "OPEN"

    if ( ( trade_data['TRADE'] != 'OK') and ( market_open_time <= current_time ) and  ( market_intermediate_time > current_time ) and ( current_time.minute % 5 ) == 0  and ( current_time.second == 00 )):

        sample = yf.download( symbols , start=today , end=tomorrow , interval='5m' )

        DateTime = list(sample.index[:-1])
        if ( len(DateTime[:-2]) >= 2 ):
            Open = sample['Open'][:-1]
            Close = sample['Close'][:-1]
            High = sample['High'][:-1]
            Low = sample['Low'][:-1]
            Volume = sample['Volume'][:-1]
            Prev_Volume = prev_sample['Volume'][:-1]
            for ticker in symbols:
                O = list(Open[ticker])
                H = list(High[ticker])
                L = list(Low[ticker])
                C = list(Close[ticker])
                CV = list(Volume[ticker])
                PV = list(Prev_Volume[ticker])
                MV = max(CV[:-2])
                MH = max(H)
                ML = min(L)
                PV_Avg  = sum(PV[35:])/40

                if ( C[-1] < 80 and C[-1] > 50 ):
                    if ( MH - ML >= 2 ):
                        if CV[-2] > (PV_Avg*6) :
                            if ( MV < CV[-2] ):
                                if ( C[-2] - O[-2] ) > 0.4 or ( O[-2] - C[-2] ) > 0.4 or ( ( H[-2] - L[-2] ) > 1 ):
                                    if  ( CV[-3] != 0 ) and ( ( CV[-2]/CV[-3] ) >= 1.5 ):
                                        if ( CV[-1] != 0 ) and ( (CV[-2]/CV[-1]) >= 1.5 ):
                                            if ( O[-1] - C[-1] ) >= 0.2 :
                                                # place order
                                                print(current_time.strftime("%Y-%m-%d %H:%M:%S"),'Sell Order',ticker)
                                                # time.sleep(5)
                                                # after 5 second get position status of order and pls conform trade in position
                                                # print(market_time[i],'Get Position',ticker)
                                                # position = kite.positions()
                                                # users = pd.read_json('users.json', typ='series')
                                                # #  if condtion true
                                                # user = users['SVM041']
                                                trade_data['POS'] = 'SELL'
                                                trade_data['TRADE'] = 'OK'
                                                trade_data['SELL_PRICE'] = C[-1] # this should be from sell order response
                                                current_time = datetime.now()
                                                trade_data['SELL_TIME'] = current_time.strftime("%Y-%m-%d %H:%M:%S")
                                                trade_data['TRADE_SYMBOL'] = ticker
                                                users['TRADE_DATA'] = dict(trade_data)
                                                # print(ticker,'Sell Position')
                                                saveCandleToJsonFile('users',users)
                                                tryToGetTarget()
                                                saveUserToHistory()

    else:
        print("Target date: "+today+" "+"Time Now: "+str(hour)+":"+str(minute)+":"+str(second)+" "+market_status+" "+trade_data['TRADE_SYMBOL'])
        if ( current_time > market_close_time ):
            market_status = "CLOSED"
            saveUserToHistory()
            
            if ( trade_data['POS'] != 'EXIT' and trade_data['TRADE'] == 'OK' ):
                sample = yf.download( trade_data['TRADE_SYMBOL'] , start=today , end=tomorrow , interval='5m' )
                trade_data['POS'] = 'EXIT'
                print(current_time, trade_data['TRADE_SYMBOL'], 'Squre off')
                print("Price",sample['Close'][-1]) 
                trade_data['BUY_PRICE'] = sample['Close'][-1] # this should be from buy order response
                trade_data['BUY_TIME'] = current_time.strftime("%Y-%m-%d %H:%M:%S")
                trade_data['PNL'] = ( trade_data['SELL_PRICE'] - trade_data['BUY_PRICE'] ) * user['QTY']  # this should be from buy position response
                users['TRADE_DATA'] = dict(trade_data)
                saveCandleToJsonFile('users',users)
                saveUserToHistory()
            
            resetUser()
    time.sleep(1)    