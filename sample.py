import pandas as pd
import numpy as np
import yfinance as yf
import requests
import time
import json

from datetime import datetime, timedelta

def checkValue(val):
    if val is None:
        return False
    elif not pd.isna(x):
        return False
    else:
        return True

i = 0
# while True:
#     current_time = datetime.now()
#     print("Time now : ",current_time)
#     # if current_time.second == 57 :
#     sample = yf.download( "BHEL.NS" , start='2023-11-15' , end='2023-11-16' )
#     C1 = sample['Close'][-1]
#     V1 = sample['Volume'][-1]
#     time.sleep(1)
#     sample = yf.download( "BHEL.NS" , start='2023-11-15' , end='2023-11-16' )
#     C2 = sample['Close'][-1]
#     V2 = sample['Volume'][-1]
#     C = C2 - C1
#     V = V2 - V1
#     print(C,V)
#     i = i+1
#     time.sleep(1)


# symbols = ['RTNINDIA.NS','GEOJITFSL.NS','BHEL.NS']

symbols = [
    # "SUBEXLTD.NS",
    # "PFS.NS",
    # # "GMRP&UI.NS",
    # "ITBEES.NS",
    # "RAMASTEEL.NS",
    # "PROZONER.NS",
    # # "SUZLON.NS",
    # "IRB.NS",
    # "TRIDENT.NS",
    # "MOREPENLAB.NS",
    # "UCOBANK.NS",
    # # "ATL.NS",
    # "IOB.NS",
    # "PSB.NS",
    # "NSLNISP.NS",
    # # "SIGACHI.NS",
    # "TV18BRDCST.NS",
    # "EASEMYTRIP.NS",
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
    # "MRPL.NS",
    # "IDFC.NS",
    # "ZOMATO.NS",
    # "TATASTEEL.NS",
    # "GAIL.NS",
    # "GPPL.NS",
    # "IEX.NS",
    # "RCF.NS",
    # "BHEL.NS",
    # "ENGINERSIN.NS",
    # "ASHOKA.NS",
    # "BEL.NS",
    # "HEMIPROP.NS",
    # "CUB.NS",
    # "SCI.NS",
    # "MANAPPURAM.NS",
    # "NYKAA.NS",
    # "NLCINDIA.NS",
    # "DELTACORP.NS",
    # "L&TFH.NS",
    # "IRCON.NS",
    # "FEDERALBNK.NS",
    # "HINDCOPPER.NS",
    # "WELSPUNIND.NS",
    # "NCC.NS",
    # "KARURVYSYA.NS",
    # "GIPCL.NS",
    # "RVNL.NS",
    # "BOMDYEING.NS",
    # "NMDC.NS",
    # "TIMETECHNO.NS",
    # "IBULHSGFIN.NS",
    # "ASHOKLEY.NS",
    # "ABCAPITAL.NS",
    # "INDUSTOWER.NS",
    # "ONGC.NS",
    # "VPRPL.NS",
    # "GSFC.NS",
    # "PCBL.NS",
    # "PETRONET.NS"
]

i=4

prev_day = '2023-11-13'
prev_next_day = '2023-11-14'

today = '2023-11-15'
tomorrow = '2023-11-16'

users = dict(pd.read_json('users-1.json', typ='series'))
trade_data = users['TRADE_DATA']

prev_sample = yf.download( symbols , start=prev_day , end=prev_next_day , interval='5m' )

market_time=['09:15', '09:20', '09:25', '09:30', '09:35', '09:40', '09:45', '09:50', '09:55', '10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55', '11:00', '11:05', '11:10', '11:15', '11:20', '11:25', '11:30', '11:35', '11:40', '11:45', '11:50', '11:55', '12:00', '12:05', '12:10', '12:15', '12:20', '12:25', '12:30', '12:35', '12:40', '12:45', '12:50', '12:55', '13:00', '13:05', '13:10', '13:15', '13:20', '13:25', '13:30', '13:35', '13:40', '13:45', '13:50', '13:55', '14:00', '14:05', '14:10', '14:15', '14:20', '14:25', '14:30', '14:35', '14:40', '14:45', '14:50', '14:55', '15:00', '15:05', '15:10', '15:15', '15:20', '15:25']

market_status = "CLOSED"

# users = pd.read_json('tradeHistory/'+tomorrow+'.json', typ='series')
# users['USER']='SVM043'
# users = dict(users)
# saveCandleToJsonFile('tradeHistory/'+tomorrow,users)


# trade_data = dict([("TRADE", ''), ("TRADE_SYMBOL", ''), ("POS", ''), ("SELL_PRICE", ''), ("SELL_TIME", ''), ("BUY_PRICE", ''), ("BUY_TIME", ''), ("QTY", 1), ("PNL", '') ])
# trade_data['USER']='SVM041'
# saveCandleToJsonFile('tradeHistory/'+tomorrow,trade_data)


# while True:
#     prev_sample = yf.download( symbols , start=today , end=tomorrow , interval='5m' )
#     print("Sample",prev_sample)
#     time.sleep(1)
# print("sample",prev_sample)


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


def saveUserToHistory():
    users = dict(pd.read_json('users-1.json', typ='series'))
    history = dict(users['TRADE_DATA'])
    history['USER']='SVM041'
    saveCandleToJsonFile('tradeHistory/'+today,history)


def saveCandleToJsonFile( filename, data ):
    jsonString = json.dumps(data)
    with open(filename+".json", "w") as outfile:
        outfile.write(jsonString)

def tryToGetTarget(i):
    while True:
        current_time = datetime.now()
        users = dict(pd.read_json('users-1.json', typ='series'))
        trade_data = users['TRADE_DATA']
        
        if ( ( current_time.minute % 5 ) == 0  ) and ( current_time.second == 00 ):
            time.sleep(2)

        if( trade_data['POS']=='SELL'):
            i=i+1
            sample = yf.download( trade_data['TRADE_SYMBOL'] , start=today , end=tomorrow , interval='5m' )
            DateTime = list(sample.index[:i])
            Close = list(sample['Close'][:i])
            if (not (trade_data['SELL_PRICE'] is None)) and ( len( Close ) > 0 ) and ( ( trade_data['SELL_PRICE'] - 0.7 ) > Close[-1] ):
                        print(DateTime[-1].strftime("%Y-%m-%d %H:%M:%S"),'Buy Order',trade_data['TRADE_SYMBOL'])
        #               place buy order wait for conformation buy checking postion from kite 
                        # time.sleep(5)
                        # after 5 second get position status of order and pls conform trade exit position
                        # print(market_time[i],'Get Position',ticker)
        #               if true
                        trade_data['POS'] = 'EXIT'
                        # print("Price",sample['Close'][-1])
                        trade_data['BUY_PRICE'] = Close[-1] # this should be from buy order response
                        trade_data['BUY_TIME'] = DateTime[-1].strftime("%Y-%m-%d %H:%M:%S")
                        trade_data['PNL'] = ( trade_data['SELL_PRICE'] - trade_data['BUY_PRICE'] ) * trade_data['QTY']  # this should be from buy position response
                        users['TRADE_DATA'] = dict(trade_data)
                        
                        saveCandleToJsonFile('users-1',users)
                        saveUserToHistory()
                        # history = pd.read_json('tradeHistory.json', typ='series')
                        # history[today] = users
                        # saveCandleToJsonFile('tradeHistory',history)
                        # print(market_time[i],ticker,'Exit Position')
                        break
        #               place order is failed then try until sucesss
        time.sleep(1)
        

if ( trade_data['POS'] == 'SELL' and trade_data['TRADE'] == 'OK' ):
    tryToGetTarget(i)


while True:
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    # 9, 34, 59)
    market_open_time = datetime(year, month, day, 22, 15, 59)
    market_intermediate_time = datetime(year, month, day, 23, 40, 00)
    market_close_time = datetime(year, month, day, 23, 55, 00)

    users = dict(pd.read_json('users-1.json', typ='series'))
    trade_data = dict(users['TRADE_DATA'])
    if ( market_open_time < current_time ) and  ( market_intermediate_time > current_time ):
        market_status = "OPEN"

    if ( ( trade_data['TRADE'] != 'OK') and ( market_open_time < current_time ) and  ( market_intermediate_time > current_time ) and ( current_time.minute % 1 ) == 0  and (current_time.second % 10) == 00 ):

        sample = yf.download( symbols , start=today , end=tomorrow , interval='5m' )
        i = i + 1
        DateTime = list(sample.index[:i])
        if ( len(DateTime[:-2]) >= 2 ):
            Open = sample['Open'][:i]
            Close = sample['Close'][:i]
            High = sample['High'][:i]
            Low = sample['Low'][:i]
            Volume = sample['Volume'][:i]
            Prev_Volume = prev_sample['Volume'][:i]
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

                # if( checkValue(C[-1]) and checkValue(CV[-2]) and checkValue(C[-2])  and checkValue(C[-1]) and checkValue(O[-2])  and checkValue(O[-1]) and checkValue(H[-2]) and checkValue(L[-2]) and checkValue(CV[-3]) and checkValue(CV[-2]) and checkValue(CV[-1]) ):

                if ( C[-1] < 80 and C[-1] > 50 ):
                    if ( MH - ML >= 2 ):
                        if CV[-2] > (PV_Avg*6) :
                            if ( MV < CV[-2] ):
                                if ( C[-2] - O[-2] ) > 0.4 or ( O[-2] - C[-2] ) > 0.4 or ( ( H[-2] - L[-2] ) > 1 ):
                                    if  ( CV[-3] != 0 ) and ( ( CV[-2]/CV[-3] ) >= 1.5 ):
                                        if ( CV[-1] != 0 ) and ( (CV[-2]/CV[-1]) >= 1.5 ):
                                            if ( O[-1] - C[-1] ) >= 0.2 :
                                                # place order
                                                print(DateTime[-1].strftime("%Y-%m-%d %H:%M:%S"),'Sell Order',ticker)
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
                                                trade_data['SELL_TIME'] = DateTime[-1].strftime("%Y-%m-%d %H:%M:%S")
                                                trade_data['TRADE_SYMBOL'] = ticker
                                                users['TRADE_DATA'] = dict(trade_data)
                                                # print(ticker,'Sell Position')
                                                saveCandleToJsonFile('users-1',users)
                                                tryToGetTarget(i)
                                                saveUserToHistory()

    else:
        print("Market Time :", market_time[i] ,"Time Now :",current_time,market_status,trade_data['TRADE'])
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
                trade_data['PNL'] = (trade_data['SELL_PRICE']-trade_data['BUY_PRICE'] ) * user['QTY']  # this should be from buy position response
                users['TRADE_DATA'] = dict(trade_data)
                saveCandleToJsonFile('users-1',users)
                saveUserToHistory()
        if( trade_data['POS'] == 'EXIT' and trade_data['TRADE'] == 'OK' ):
            i=i+1
        if (i>=len(market_time)):
            break
    time.sleep(1)

    


    
    


    