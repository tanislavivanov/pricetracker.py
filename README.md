
## How to use

### Step 1

Install the required prerequisites:

```python
  pip install bs4 
``` 
-- or --
```python
  pip install bs4 --user
```

### Step 2
Open *pricetracker.py* with your IDE and change the following tags:
1. URL = **"PRODUCT_LINK_HERE"** - Enter the URL of the product page you want to track the price of.
2. wh = **"WEBHOOK_URL_HERE"** - Enter the Discord Webhook URL. This can be found in Channel Settings > Integrations > Webhooks > Copy URL.
3. results = soup.find(class_=**"REPLACE_WITH_PARENT_CLASS"**) - Type the name of the parent (usually div) class of the element.
4. price = results.find_all("div", class_=**"REPLACE_WITH_ELEMENT_CLASS"**) - Type the html (usually div) class of the element.

> *Repeat steps 3. and 4. for lines 43 and 45 aswell.*

### Step 3 (optional)
Change the default messages of the print() and webhook data {[]} entries.

### Step 4
Run with 
```python
  py ./pricetracker.py
```