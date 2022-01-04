from django.http import *
from django.shortcuts import render

from MyAppWeb.DB.DB import Database


def get_shopping_cart(request):
    if request.method == 'GET':
        return render(request, "shoping_car.html")
    else:
        uid = -1
        try:
            uid = request.COOKIES.get('user_id')
        except Exception as e:
            print(e)

        goods_list = []

        db = Database()
        goods_ids = db.select_more('shopping_cart', "user_id='" + uid + "'", 'goods_id')
        sum = 0
        for goods_id in goods_ids:
            temp = db.select_one('app01_goods', "goods_id=" + str(goods_id['goods_id']),
                                 'goods_name,goods_classify_id,goods_pic_path,goods_price')
            print(temp['goods_classify_id'])
            classify_name = db.select_one('app01_classify', 'classify_id=' + str(temp['goods_classify_id']),
                                          'classify_name')['classify_name']
            goods = {"goods_id": str(goods_id['goods_id']), "goods_name": temp['goods_name'],
                     "goods_classify": classify_name,
                     "goods_pic_path": temp['goods_pic_path'],
                     "price": temp['goods_price']}
            goods_list.append(goods)
            sum += temp['goods_price']
        goods_list.append({"price_sum": str(sum)})
        return HttpResponse(str(goods_list).replace("'", "\""))
