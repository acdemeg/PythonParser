from item_collector import getRowItems, createItemsList, saveBase64Images


# parsing goods form https://www.onlinetrade.ru
def main():
    domain = "https://www.onlinetrade.ru"
    itemsArr = getRowItems(domain + "/catalogue/smart_chasy-c1238/")
    itemsSet = createItemsList(itemsArr, domain)
    saveBase64Images(itemsSet)
    return ""


if __name__ == '__main__':
    main()
