<<<<<<< HEAD
from django.conf.urls import url, include
=======
from django.conf.urls import url
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e

from apps.goods import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(\d+)$', views.DetailView.as_view(), name='detail'),
    url(r'^list/(\d+)/(\d+)$', views.ListView.as_view(), name='list'),
=======
    url("^index$", views.Goods_View.as_view(), name="index"),
    url("^logout$", views.Logout_View.as_view(), name="logout"),
    url(r'^detail/(?P<sku_id>\d+)$', views.DetailView.as_view(), name='detail'),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
]
