import requests
import json
import csv
import sys
import time
from time import gmtime, strftime

#Variables
station_id = 'cc04628a-674a-4b3b-8f58-70943806eeb5'     #id of wanted gas station
type = 'diesel'                                         #type of gas for price ('diesel', 'e5', 'e10')
threshold = 2.4                                         #threshold for Telegram notification
time_interval = 60 * 10                                 #wait time between API-Calls
filename = 'diesel.csv'                                 #filename for csv safes

#fetches diesel price from gasstation defined under variables
def getPrice(api_key):
    r = requests.get(f'https://creativecommons.tankerkoenig.de/json/detail.php?id={station_id}&apikey={api_key}')
    data = r.json()
    prices = data['station']
    price = prices[type]
    print("Price is: ", price)
    return price

#sends msg to Telegram chat with chat_id via bot with bot_token
def sendMessage(bot_token, chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    requests.get(url)

#save price to csv
def saveToCsv(price):
    date = strftime("%Y-%m-%d", gmtime())
    hour = strftime("%H:%M:%S", gmtime())
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, hour, price])
    print('polled at ')
    print(date)
    print(hour)
    print(price)
    print('\n')

#get Tokens
def getTokens():
    with open('token.txt', 'r') as file:
        data = file.read().split('\n')
        input = []
        for line in data:
            if len(line) > 2:
                number, name = line.split(';')
                input.append(number)
    bot_token = input[0]
    input.pop(0)
    api_key = input[0]
    input.pop(0)
    return bot_token, api_key, input



def main():
    #Setup Tokens & Keys
    bot_token, api_key, chat_ids = getTokens()

    while True:
        price = getPrice(api_key)
        saveToCsv(price)
        #if price < threshold send message via TelegramBot
        if price < threshold:
            for chat_id in chat_ids:
                sendMessage(bot_token, chat_id, f'Diesel bei MTB: {price}')

        #wait time intervall
        time.sleep(time_interval)


###############################################################################################################
        
if __name__ == '__main__':
    main()
