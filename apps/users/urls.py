from django.conf.urls import url

from apps.users import views

urlpatterns = [
<<<<<<< HEAD
    # 处理登录操作
    # url(r'^do_register$', views.do_register, name='do_register'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),  # 注册
    url(r'^active/(.+)$', views.ActiveView.as_view(), name='active'),  # 激活
    url(r'^login/$', views.LoginView.as_view(), name='login'),  # 登录
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),  # 退出

    url(r'^address$', views.UserAddressView.as_view(), name='address'),  # 用户中心:地址
    # url(r'^orders$', views.UserOrderView.as_view(), name='orders'),  # 用户中心:订单
    url(r'^info$', views.UserInfoView.as_view(), name='info'),  # 用户中心:个人信息
    url(r'^orders/(\d+)$', views.UserOrderView.as_view(), name='orders'),  # 用户订单

=======
    # 测试
    url(r"^show_login$", views.show_login),
    url(r"^do_login$", views.do_login),
    # 注册
    url(r"^Register$", views.RegisterView.as_view(), name="Register"),
    # 激活
    url(r'^active/(.+)$', views.ActiveView.as_view(), name='active'),
    # 登陆
    url(r'^login$', views.Login_View.as_view(), name='login'),
    # 用户中心-个人信息
    url(r'^center_info$', views.Center_Info.as_view(), name='info'),
    # 用户中心-全部订单
    url(r'^center_order$', views.Center_Order.as_view(), name='order'),
    # 用户中心-收货地址
    url(r'^center_site$', views.Center_Site.as_view(), name='site'),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
]
