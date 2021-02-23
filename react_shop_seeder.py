import urllib.request
import json


# seeding items to heroku-react-app
def seedGoods(itemsSet):

    for item in itemsSet:
        req = urllib.request.Request("https://react-node-online-shop.herokuapp.com/api/products", method="POST")
        req.add_header('Content-Type', 'application/json')

        data = {
            "category": "Все товары    ",
            "count": "100",
            "description": item.shortDesc,
            "detailInfo": item.fullDesc,
            "nameProduct": item.title,
            "pathImage": item.imageBase64,
            "price": item.price
        }

        data = json.dumps(data)
        item = data.encode()

        res = urllib.request.urlopen(req, data=item).read()
        print(res)

    pass
