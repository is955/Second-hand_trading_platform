from django.http import *
from django.shortcuts import render

from MyAppWeb.DB.DB import Database


def registered(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        # password = str(hash(password))
        email = request.POST['email']

        db = Database()

        num = db.select_more('user', "username='" + username + "'", '*')
        if len(num) != 0:
            return HttpResponse('用户名已存在')
        else:
            temp = db.insert('user', {"username": username, "password": password, "email": email})
            db.close()
            if temp == 0:
                # return HttpResponse('success')
                return HttpResponseRedirect('/login')
            else:
                return HttpResponse('Registered False!')
