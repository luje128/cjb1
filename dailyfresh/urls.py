<<<<<<< HEAD
=======
"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
from django.conf.urls import include, url
from django.contrib import admin
import tinymce.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD

    url(r'^users/', include('apps.users.urls', namespace='users')),  # 用户模块
    url(r'^cart/', include('apps.cart.urls', namespace='cart')),  # 购物车模块
    url(r'^orders/', include('apps.orders.urls', namespace='orders')),  # 订单模块
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('apps.users.urls')),
    url(r'^', include('apps.goods.urls', namespace='goods')),  # 商品模块
    url(r'^search/', include('haystack.urls')),


=======
    url(r'^users/', include("apps.users.urls", namespace="users")),
    url(r'^orders/', include("apps.orders.urls", namespace="orders")),
    url(r'^goods/', include("apps.goods.urls", namespace="goods")),
    url(r'^cart/', include("apps.cart.urls", namespace="cart")),
    url(r'^tinymce/', include("tinymce.urls")),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
]
