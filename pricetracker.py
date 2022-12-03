import requests
from bs4 import BeautifulSoup
import re
import time
import socket

# URL of the product you want to track the price of.
# Should begin with either https:// or http://
# Should be a valid URL!
URL = "PRODUCT_LINK_HERE"

# Discord Webhook URL
# Can be found in Channel Settings > Integrations > Webhooks > Copy URL
wh = "WEBHOOK_URL_HERE"

# For all Webhook Parameters, see https://discord.com/developers/docs/resources/webhook#execute-webhook
data = {
    "username": "PRICETRACKER",
    "content": "[PRICETRACKER] Running on **"+socket.gethostbyname(socket.gethostname())+"**\nTracking price of **"+URL+"**"
}

result = requests.post(wh, json = data)

# Fetch original price on run.
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="REPLACE_WITH_PARENT_CLASS") # Replace with the name of the parent class or change "class_" to "id" if you want to use an id instead.

price = results.find_all("div", class_="REPLACE_WITH_ELEMENT_CLASS") # Replace with the name of the element class or change "class_" to "id" if you want to use an id instead.

oldprice = str(price[0])
oldprice = re.findall(r'\b\d+\b', oldprice)
oldprice = oldprice[0]+oldprice[1]+"."+oldprice[2]
oldprice = float(oldprice)


while True:
    
    #FETCH NEW PRICE
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="REPLACE_WITH_PARENT_CLASS")

    price = results.find_all("div", class_="REPLACE_WITH_ELEMENT_CLASS")

    newprice = str(price[0])
    newprice = re.findall(r'\b\d+\b', newprice)
    newprice = newprice[0]+newprice[1]+"."+newprice[2]
    newprice = float(newprice)
    if(newprice!=oldprice):
        print("\n[PRICETRACKER] There is a price change!")
        print("Was "+str(oldprice)+" - Now "+str(newprice))

        data = {
            "username": "PRICETRACKER",
            "content": "[PRICETRACKER] There is a price change! \nWas **"+str(oldprice)+"** - Now **"+str(newprice)+"**"
        }

        result = requests.post(wh, json = data)

        oldprice=newprice
    else:
        print("\n[PRICETRACKER] No price change.")
    time.sleep(100) # The amount of seconds between price checks.
                    # We recommend 100 or 200 due to the stress you may be putting on the site and the risk of being rate limited/IP-restricted.