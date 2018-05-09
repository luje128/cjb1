import re
<<<<<<< HEAD
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django_redis import get_redis_connection
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
from redis import StrictRedis
from apps.goods.models import GoodsSKU
from apps.orders.models import OrderInfo, OrderGoods
from apps.users.models import User, Address
from dailyfresh import settings
from utils.LoginRequiredMixin import LoginRequiredMixin
from celery_tasks.tasks import send_active_mail


class RegisterView(View):
    """注册视图"""

    def get(self, request):
        """进入注册界面 """
        return render(request, 'register.html')

    def post(self, request):
        """实现注册功能 """

        # 获取post请求参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        allow = request.POST.get('allow')  # 用户协议， 勾选后得到：on

        # todo: 校验参数合法性
        # 判断参数不能为空
        if not all([username, password, password2, email]):
            # return redirect('/users/register')
            return render(request, 'register.html', {'errmsg': '参数不能为空'})

        # 判断两次输入的密码一致
        if password != password2:
            return render(request, 'register.html', {'errmsg': '两次输入的密码不一致'})

        # 判断邮箱合法
        if not re.match('^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱不合法'})

        # 判断是否勾选用户协议(勾选后得到：on)
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请勾选用户协议'})

        # 处理业务： 保存用户到数据库表中
        # django提供的方法，会对密码进行加密
        user = None
        try:
            user = User.objects.create_user(username, email, password)  # type: User
            # 修改用户状态为未激活
            user.is_active = False
            user.save()
        except IntegrityError:
            # 判断用户是否存在
            return render(request, 'register.html', {'errmsg': '用户已存在'})

        # todo: 发送激活邮件
        token = user.generate_active_token()
        # 方式1：同步发送：如果网络卡的话会延迟,会阻塞
        # RegisterView.send_active_mail(username, email, token)
        # sleep(5)
        # 方式2：使用celery异步发送：不会阻塞
        # 会保存方法名参数等到Redis数据库中
        send_active_mail.delay(username, email, token)

        # 响应请求
        return render(request, 'login.html')

        # @staticmethod
        # def send_active_mail(username, email, token):
        #     """发送激活邮件"""
        #     subject = '天天生鲜激活邮件'  # 标题，必须指定
        #     message = ''  # 正文
        #     from_email = settings.EMAIL_FROM  # 发件人
        #     recipient_list = [email]  # 收件人
        #     # 正文 （带有html样式）
        #     html_message = ('<h3>尊敬的%s：感谢注册天天生鲜</h3>'
        #                     '请点击以下链接激活您的帐号:<br/>'
        #                     '<a href="http://127.0.0.1:8000/users/active/%s">'
        #                     'http://127.0.0.1:8000/users/active/%s</a>'
        #                     ) % (username, token, token)
        #
        #     send_mail(subject, message, from_email, recipient_list,
        #               html_message=html_message)


class ActiveView(View):
    def get(self, request, token: str):
        """
        用户激活
        :param request:
        :param token: 对字典 {'confirm':用户id} 进行加密后得到的字符串
        :return:
        """
        try:
            # 解密token
            s = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
            # 字符串 -> bytes
            # dict_data = s.loads(token.encode())
            dict_data = s.loads(token)
        except SignatureExpired:
            # 判断是否失效
            return HttpResponse('激活链接已经失效')

        # 获取用户id
        user_id = dict_data.get('confirm')
        # 修改字段为已激活
        User.objects.filter(id=user_id).update(is_active=True)
        # 响应请求
        return HttpResponse('激活成功,请登录')


class LoginView(View):
    def get(self, request):
        """进入登录界面"""
        return render(request, 'login.html')

    def post(self, request):
        """处理登录操作"""

        # 获取登录参数
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 校验参数合法性
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '请求参数不完整'})

        # 通过 django 提供的authenticate方法，
        # 验证用户名和密码是否正确
        user = authenticate(username=username, password=password)

        # 用户名或密码不正确
        if user is None:
            return render(request, 'login.html', {'errmsg': '用户名或密码不正确'})

        if not user.is_active:  # 注册账号未激活
            # 用户未激活
            return render(request, 'login.html', {'errmsg': '请先激活账号'})

        # 通过django的login方法，保存登录用户状态（使用session）
        login(request, user)
        # 获取是否勾选'记住用户名'
        remember = request.POST.get('remember')
        # 判断是否是否勾选'记住用户名'
        if remember != 'on':
            # 没有勾选，设置session数据有效期为关闭浏览器后失效
            request.session.set_expiry(0)
        else:
            # 已勾选，设置session数据有效期为两周
            request.session.set_expiry(None)
        # 登录成功后,要跳转到NEXT指向的界面
        next = request.GET.get('next')
        if next:
            # 不为空,则跳转到next指向的界面
            return redirect(next)
        else:
            # 响应请求，返回html界面 (进入首页)
            return redirect(reverse('goods:index'))


class LogoutView(View):
    """退出登录"""

    def get(self, request):
        """处理退出登录逻辑"""

        # 由Django用户认证系统完成：会清理cookie
        # 和session,request参数中有user对象
        logout(request)

        # 退出后跳转：由产品经理设计
        return redirect(reverse('goods:index'))


class UserInfoView(LoginRequiredMixin, View):
    """用户中心:个人信息界面"""

    def get(self, request):
        # todo: 从Redis中读取当前登录用户浏览过的商品
        strict_redis = get_redis_connection('default')  # type: StrictRedis
        # 读取所有的商品ID,返回一个列表
        key = 'history_%s' % request.user.id
        # 最多只取5个商品ID[3,1,2]
        sku_ids = strict_redis.lrange(key, 0, 4)
        # 根据商品ID,查询出商品对象

        # skus = GoodsSKU.objects.filter(id__in=sku_ids)
        skus = []
        for sku_id in sku_ids:
            sku = GoodsSKU.objects.get(id=sku_id)
            skus.append(sku)

=======

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View
from django_redis import get_redis_connection
from itsdangerous import SignatureExpired, TimedJSONWebSignatureSerializer

from Mix.Login import LoginRequiredMixin
from apps.goods.models import GoodsSKU
from apps.users.models import User, Address
from dailyfresh import settings
from celery_tasks import tasks


# 测试一
def show_login(request):
    return render(request, "login.html")


# 测试二
def do_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username != "admin" and password != 12345:
        return render(request, "login.html")
    return HttpResponse("go")


# 注册类
class RegisterView(View):
    def get(self, request):
        # 进入页面
        return render(request, "register.html")

    def post(self, request):
        # 实现注册
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        allow = request.POST.get("allow")
        if not all([username, password, password2, email]):
            return render(request, "register.html", {"what": "您有信息未填写完整!", "isalert": 1})
        if password != password2:
            return render(request, "register.html", {"what": "密码错误，请重新输入!"})
        if allow != "on":
            return render(request, "register.html", {"what": "请点击同意用户协议!"})
        if not re.match(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$", email):
            return render(request, "register.html", {"what": "邮箱格式错误，请重新输入！"})
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            # 默认激活，现在更改为未激活
            user.is_active = False
            # 保存
            user.save()
        except IntegrityError:
            return render(request, 'register.html', {'what': '用户名已存在'})

        # todo:发送激活邮件
        token = user.generate_active_token()
        # 同步发送会阻塞
        RegisterView.send_active_email(username, email, token)
        # celery异步发送
        # tasks.send_active_email.delay(username, email, token)

        return redirect("/users/login")

    @staticmethod
    def send_active_email(username, receiver, token):
        """发送激活邮件"""
        subject = "天天生鲜用户激活"  # 标题, 不能为空，否则报错
        message = ""  # 邮件正文(纯文本)
        sender = settings.EMAIL_FROM  # 发件人
        receivers = [receiver]  # 接收人, 需要是列表
        # 邮件正文(带html样式)
        html_message = ('<h3>尊敬的%s：感谢注册天天生鲜</h3>'
                        '请点击以下链接激活您的帐号:<br/>'
                        '<a href="http://127.0.0.1:8000/users/active/%s">'
                        'http://127.0.0.1:8000/users/active/%s</a>'
                        ) % (username, token, token)
        send_mail(subject, message, sender, receivers,
                  html_message=html_message)


# 数据加密类
class ActiveView(View):
    def get(self, request, token: str):
        """
        激活注册用户
        :param request:
        :param token: 对{'confirm':用户id}字典进行加密后的结果
        :return:
        """
        # 解密数据，得到字典
        dict_data = None
        try:
            s = TimedJSONWebSignatureSerializer(
                settings.SECRET_KEY, 3600 * 24)
            dict_data = s.loads(token.encode())  # type: dict
        except SignatureExpired:
            # 激活链接已经过期
            return HttpResponse('激活链接已经过期')

        # 获取用id
        user_id = dict_data.get('confirm')

        # 激活用户，修改表字段is_active=True
        User.objects.filter(id=user_id).update(is_active=True)

        # 响应请求
        return HttpResponse('激活成功，进入登录界面')


# 登陆类
class Login_View(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        if not all([username, password]):
            return render(request, "login.html", {"content": "输入不完整"})
        # 判断用户名和密码是否正确
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html", {"content": "输入有误"})
        if user.is_active is False:
            return render(request, "login.html", {"content": "账号未激活"})
        login(request, user)
        if remember == "on":
            request.session.set_expiry(None)
        else:
            request.session.set_expiry(0)

        next = request.GET.get('next')
        if next is None:
            # 如果是直接登陆成功，就重定向到首页
            return redirect(reverse('goods:index'))
        else:
            # 如果是用户中心重定向到登陆页面，就回到用户中心
            return redirect(next)


# 用户中心-个人信息
class Center_Info(LoginRequiredMixin, View):
    def get(self, request):
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        # 获取用户对象
        user = request.user

        # 查询用户最新添加的地址
        try:
            address = user.address_set.latest('create_time')
<<<<<<< HEAD
        except Exception:
            address = None

=======
        except Address.DoesNotExist:
            address = None

        # 从redis查询出用户的商品浏览记录，返回的是列表例:a=[a1,a2]
        strict_redis = get_redis_connection("default")
        # 设置用户的id为键名
        key = "history_%s" % request.user.id
        # 最多5条记录，例：[1,2,3,4]
        goods_ids = strict_redis.lrange(key, 0, 4)
        # 真正的商品浏览顺序为原来保存在redis中的顺序
        # 手动排序，逐个查询，逐个添加
        skus = []
        for id in goods_ids:
            try:
                skus.append(GoodsSKU.objects.get(id=id))
            except GoodsSKU.DoesNotExist:
                pass

>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        # 定义模板数据
        data = {
            # 不需要主动传，django会传
            # 'user': user,
<<<<<<< HEAD
            'which_page': 1,
            'address': address,
            'skus': skus
=======
            'page': 1,
            'address': address,
            "skus": skus,
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        }

        # 响应请求,返回html界面
        return render(request, 'user_center_info.html', data)


<<<<<<< HEAD
class UserOrderView(LoginRequiredMixin, View):
    """
    用户订单页
    """

    def get(self, request, page_num):
        """显示订单列表界面"""

        # 查询当前用户所有订单
        orders = OrderInfo.objects.filter(
            user=request.user).order_by('-create_time')

        for order in orders:
            # 查询某一订单下所有的订单商品
            order_skus = OrderGoods.objects.filter(order=order)
            for order_sku in order_skus:
                # 计算商品的小计金额
                amount = order_sku.price * order_sku.count
                # 动态地给订单商品添加小计金额
                order_sku.amount = amount

            # 新增实例属性: 订单商品
            order.order_skus = order_skus
            # 新增实例属性: 实付金额
            order.total_pay = order.total_amount + order.trans_cost
            # 新增实例属性: 订单状态名称
            order.status_desc = OrderInfo.ORDER_STATUS.get(order.status)

        # 参数1: 所有分页数据
        # 参数2: 每页显示多少条
        paginator = Paginator(orders, 2)
        try:
            # 获取某一页数据
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)

        # 定义模板显示的数据
        context = {
            'page': page,
            'which_page': 2,
            'page_range': paginator.page_range,
        }

        # 响应请求, 返回html界面
        return render(request, 'user_center_order.html', context)


class UserAddressView(LoginRequiredMixin, View):
    """用户中心--地址界面"""

=======
# 用户中心-全部订单
class Center_Order(LoginRequiredMixin, View):
    def get(self, request):
        data = {
            "page": 2
        }
        return render(request, "user_center_order.html", data)


# 用户中心-收货地址
class Center_Site(LoginRequiredMixin, View):
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    def get(self, request):
        """显示用户地址"""
        user = request.user
        try:
            # 查询用户地址：根据创建时间排序，最近的时间在最前，取第1个地址
<<<<<<< HEAD
            # 方式1：  可能会IndexError
            address = Address.objects.filter(user=request.user) \
                .order_by('-create_time')[0]
            # 方式2： 可能会报IndexError
            # address = request.user.address_set.order_by('-create_time')[0]
            # 方式3： 可能会报DoesNotExist错误
=======
            address = Address.objects.filter(user=request.user) \
                .order_by('-create_time')[0]  # IndexError
            # IndexError
            # address = request.user.address_set.order_by('-create_time')[0]
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            address = user.address_set.latest('create_time')
        except Exception:
            address = None

        data = {
            # 不需要主动传, django会自动传
            # 'user':user,
            'address': address,
<<<<<<< HEAD
            'which_page': 3
=======
            'page': 3
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        }
        return render(request, 'user_center_site.html', data)

    def post(self, request):
        """"新增一个地址"""

        # 获取用户请求参数
        receiver = request.POST.get('receiver')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        mobile = request.POST.get('mobile')
        # 登录后django用户认证模块默认
        # 会保存user对象到request中
        user = request.user  # 当前登录用户

        # 校验参数合法性
        if not all([receiver, address, zip_code, mobile]):
<<<<<<< HEAD
            return render(request, 'user_center_site.html', {'errmsg': '参数不完整'})
=======
            return render(request, 'user_center_site.html', {'error': '参数不完整'})
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e

        # 保存地址到数据库中
        Address.objects.create(
            receiver_name=receiver,
            receiver_mobile=mobile,
            detail_addr=address,
            zip_code=zip_code,
            user=user
        )

<<<<<<< HEAD
        # 响应请求，刷新当前界面(/users/address)
        return redirect(reverse('users:address'))
=======
        # 响应请求，刷新当前界面
        return redirect(reverse('users:site'))
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
