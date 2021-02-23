from item_collector import getRowItems, createItemsList, saveBase64Images
from react_shop_seeder import seedGoods


# parsing goods form https://www.onlinetrade.ru
def main():
    domain = "https://www.onlinetrade.ru"
    itemsArr = getRowItems(domain + "/catalogue/kulery_dlya_protsessorov-c1492/")
    itemsSet = createItemsList(itemsArr, domain)
    saveBase64Images(itemsSet)
    seedGoods(itemsSet)
    pass


if __name__ == '__main__':
    main()
