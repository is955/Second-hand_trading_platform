from django.shortcuts import render

from MyAppWeb.DB.DB import Database


def detail(request):
    goods_id = request.GET['goods_id']
    db = Database()
    temp = db.select_one('app01_goods', "goods_id=" + str(goods_id),
                         'goods_name,goods_info,goods_pic_path,goods_price')
    db.close()
    return render(request, 'detail.html', {'info':temp})
