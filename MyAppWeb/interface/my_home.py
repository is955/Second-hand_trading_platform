from django.shortcuts import render

from MyAppWeb.DB.DB import Database


def my_home(request):
    # if request.method == 'GET':
    return render(request, 'myhome.html')