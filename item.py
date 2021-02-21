class Item:
    def __init__(self, price, shortDesc, title, itemLink, imageLink, fullDesc):
        self.__price = price
        self.__shortDesc = shortDesc
        self.__title = title
        self.__fullDesc = fullDesc
        self.__itemLink = itemLink
        self.__imageLink = imageLink
        self.__imageBase64 = ""

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @property
    def shortDesc(self):
        return self.__shortDesc

    @property
    def fullDesc(self):
        return self.__fullDesc

    @property
    def itemLink(self):
        return self.__itemLink

    @property
    def imageLink(self):
        return self.__imageLink

    @property
    def imageBase64(self):
        return self.__imageBase64

    @imageBase64.setter
    def imageBase64(self, imageBase64):
        self.__imageBase64 = imageBase64
