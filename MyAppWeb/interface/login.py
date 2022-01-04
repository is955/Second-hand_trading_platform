from django.http import *
from django.http import HttpResponse
from django.shortcuts import render

from MyAppWeb.DB.DB import Database


def login(request):
    if request.method == 'GET':
        user_id = request.COOKIES.get('user_id')

        if user_id is None:
            response = HttpResponse("False")
            return response
        else:
            db = Database()
            res = db.select_one('user', "user_id='" + user_id + "'", '*')
            db.close()
            response = HttpResponse(res['username'])
            return response
    else:
        username = request.POST['username']
        password = request.POST['password']
        # password = str(hash(password))
        print(password)
        db = Database()
        res = db.select_one('user', "username='" + username + "'", '*')
        db.close()
        if res['password'] == password:
            response = HttpResponse("success")
            response.set_cookie('user_id', res['user_id'], max_age=18000)
            return response
        else:
            return HttpResponse('Login False!')
