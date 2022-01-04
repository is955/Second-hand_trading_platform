import time
import uuid

from django.http import *
from django.shortcuts import render

from MyAppWeb.DB.DB import Database
from MyAppWeb.DB.DB2 import query_all, insert


def buy(request):
    user_id = request.COOKIES.get('user_id')
    if request.method == "GET":
        if user_id is not None:
            response = render(request, 'order.html')
            goods_id = request.GET["goods_id"]
            print(goods_id)
            response.set_cookie('goods_id', goods_id, max_age=600)
            return response
        else:
            return HttpResponseRedirect('main')
    if request.method == "POST":
        goods_id = request.COOKIES.get('goods_id')
        print(goods_id)
        # 通过goods_id找到买家，价格
        sql = "select user_id,goods_price from app01_goods where goods_id=%s"
        res = query_all(sql, [goods_id])
        print(str(res))
        order_id = uuid.uuid1()
        address = request.POST['address']
        phone = request.POST['phone']
        pwd = request.POST['password']
        sql1 = "select * from user where user_id=%s and password=%s"
        res1 = query_all(sql1, [user_id, pwd])
        order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        if len(res1) > 0:
            print(str(res1))
            # 支付密码验证正确插入order_form
            sql2 = "insert into order_form(order_id,seller_id,buyer_id,goods_id,order_price,create_time,order_state,shopping_address,phone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            res = insert(sql2,
                         [order_id, res[0]['user_id'], user_id, goods_id, res[0]['goods_price'], order_time, '1',
                          address,
                          phone])

            if res is None:
                return render(request, 'myhome.html')
        else:
            return HttpResponse('密码输入错误')
