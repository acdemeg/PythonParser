import urllib.request
import re


# remove all garbage from description
def prepareFullDesk(itemFullDescRow):
    return itemFullDescRow.replace(
        "><ul class=\"featureList js__backlightingClick\">", ""
    ).replace(
        "<li class=\"featureList__item\"><span class=\"gray\">", ""
    ).replace(
        "&#160;</li>", "\n").replace("</ul>", "").replace("</span>", " ")


# parse item description and image link
def getFullInfoItem(link):
    query = urllib.request.urlopen(link).read()
    pageItem = str(query, "windows-1251")

    itemImage = re.search(
        "</a></div><meta itemprop=\"image\" content=\"(.+?(png|jpg)).+?<div class=\"p__displayedItem__",
        pageItem).group(1)

    itemFullDescRow = re.search(
        "<h2>Характеристики</h2(.+)<div class=\"clear\">&nbsp;</div>(<p|<h2)",
        pageItem)

    if itemFullDescRow is None:
        itemFullDescRow = "Описание отсутствует"
    else:
        itemFullDescRow = itemFullDescRow.group(1)

    itemFullDesc = prepareFullDesk(itemFullDescRow)

    return itemImage, itemFullDesc


# parse item details form markup
def prepareDataItem(itemStr, domain):
    itemPrice = re.search(
        " title=\"\w+ цена\">(.+?) &#8381;</span>", itemStr
    ).group(1).replace("<span class=\"gray\">", "")
    itemShortDesc = re.search("title=\"Подробнее о «(.+)»\" ><img", itemStr).group(1)
    itemShortDesc = itemShortDesc.replace("&quot;", "")

    print(itemShortDesc)

    itemTitle = re.match("(.+?( |-| )){3}", itemShortDesc).group(0)
    itemLink = domain + re.search("a href=\"(.+)\" class=\"indexGoods__item__image\"", itemStr).group(1)
    itemImage, itemFullDesc = getFullInfoItem(itemLink)

    return itemPrice, itemShortDesc, itemTitle, itemLink, itemImage, itemFullDesc
