import time
import uuid

from django.http import HttpResponse

from MyAppWeb.DB.DB2 import *


def buy(request):
    # user_id = request.COOKIES['user_id']
    user_id = '1'
    if request.method == "GET":
        # cookie不存在跳转登录，存在就购买
        if (user_id != ''):
            return HttpResponse("一登陆，可以购买")
        else:
            # return render(request,'登录界面')
            return HttpResponse("请登录")
    if request.method == "POST":
        goods_id = '2'
        sql = "select user_id,goods_price from app01_goods where goods_id=%s"
        res = query_all(sql, [goods_id])
        order_id = uuid.uuid1()
        address = request.POST['address']
        phone = request.POST['phone']
        pwd = request.POST['password']
        sql1 = "select * from user where user_id=%s and password=%s"
        res1 = query_all(sql1, [user_id, pwd])
        order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        if len(res1) > 0:
            # 支付密码验证正确插入order_form
            sql2 = "insert into order_form(order_id,seller_id,buyer_id,goods_id,order_price,create_time,order_state,shopping_address,phone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            res = insert(sql2,
                         [order_id, res[0]['user_id'], user_id, goods_id, res[0]['goods_price'], order_time, '1',
                          address,
                          phone])
            if res == None:
                # return render(request,'购买成功跳转的页面')
                return HttpResponse('购买成功')
        else:
            return HttpResponse('密码输入错误')


def del_goods(request):
    goods_id = request.POST["goods_id"]
    sql = "update app01_goods set is_active=%s where goods_id=%s"
    res = excute(sql, [0, goods_id])
    if res:
        return HttpResponse("ok")
    else:
        return HttpResponse("下嘉失败")
