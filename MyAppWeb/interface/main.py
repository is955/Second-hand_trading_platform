from django.shortcuts import render

from MyAppWeb.DB.DB import Database


def main_func(request):
    if request.method == 'GET':
        db = Database()
        goods = db.select_more('app01_goods', "1=1", '*')
        fl = db.select_more('app01_classify', "1=1", '*')
        db.close()

        return render(request, 'main.html', {"res_goods": goods, "res_classify": fl})
