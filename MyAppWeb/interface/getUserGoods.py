# 查询用户上传过的商品
from django.http import HttpResponse

from MyAppWeb.DB.DB2 import *


# 查询用户上传过的商品
def get_by_id(request):
    # user_id=request.COOKIES.get['user_id']
    user_id = request.COOKIES.get('user_id')
    sql = 'select goods_id,goods_name,goods_price,goods_pic_path from app01_goods where user_id=%s '
    # res为None表示数据库操作成功
    res = query_all(sql, [user_id])
    return HttpResponse(str(res).replace("'", '"'))


# 根据userid查询购买过的物品
def user_buy(request):
    # user_id=request.COOKIES.get['user_id']
    user_id = request.COOKIES.get('user_id')
    sql = '''select o.order_id ,a.goods_name,a.goods_price,a.goods_pic_path 
             from order_form o,app01_goods a 
             where o.buyer_id=a.user_id and user_id=%s'''
    # res为None表示数据库操作成功
    res = query_all(sql, [user_id])
    return HttpResponse(res)
