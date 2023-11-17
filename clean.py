import json

def saveCandleToJsonFile( filename, data ):
    jsonString = json.dumps(data)
    with open(filename+".json", "w") as outfile:
        outfile.write(jsonString)

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

