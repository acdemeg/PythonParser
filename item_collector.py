import re
import base64
import urllib.request
from item_parser import prepareDataItem
from item import Item


# collate item list from page
def getNextPage(page):
    itemsRow = re.search(
        "(class=\"indexGoods__item\").+(rel=\"nofollow\">(Купить|Сообщить)</a>)",
        page).group(0)
    return itemsRow.split("<div class=\"indexGoods__item\"")


# collate items from all pages
def getRowItems(url):
    items = []

    for number in range(0, 100):
        query = urllib.request.urlopen(url + f"?page={number}")
        if query.url != url:
            page = str(query.read(), "windows-1251")
            pageItems = getNextPage(page)
            items = items + pageItems
        else:
            break

    return items


# create items set from Item objects
def createItemsList(itemsArr, domain):
    items = set()
    for item in itemsArr:
        itemPrice, itemShortDesc, itemTitle, itemLink, itemImage, itemFullDesc = prepareDataItem(item, domain)
        obj = Item(itemPrice, itemShortDesc, itemTitle, itemLink, itemImage, itemFullDesc)
        items.add(obj)

    return items


# setting base64Image string in each item
def saveBase64Images(itemsSet):
    for item in itemsSet:
        query = urllib.request.urlopen(item.imageLink)
        image = ("data:" + query.headers['Content-Type'] + ";" + "base64," +
                 str(base64.b64encode(query.read()).decode("utf-8")))
        item.imageBase64 = image

