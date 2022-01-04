"""MyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MyAppWeb.interface import registered, login,shopping_cart,main,my_home,getUserGoods,detail,buy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registered', registered.registered),
    path('login', login.login),
    path('getShopCart', shopping_cart.get_shopping_cart),
    path('main', main.main_func),
    path('myhome', my_home.my_home),
    path('getusergoods', getUserGoods.get_by_id),
    path('detail', detail.detail),
    path('buy', buy.buy),
    path('', main.main_func, name="home"),
]
