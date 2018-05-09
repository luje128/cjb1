<<<<<<< HEAD
=======
# celery服务器所在的代码需要打开这四行代码的注释
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
# django.setup()
<<<<<<< HEAD
from time import sleep

from celery import Celery
from django.core.mail import send_mail
from django.template import loader

from apps.goods.models import GoodsCategory, IndexSlideGoods, IndexPromotion, IndexCategoryGoods
from dailyfresh import settings

app = Celery('dailyfresh', broker='redis://127.0.0.1:6379/2')


@app.task
def send_active_mail(username, email, token):
    """发送激活邮件"""
    subject = '天天生鲜激活邮件'  # 标题，必须指定
    message = ''  # 正文
    from_email = settings.EMAIL_FROM  # 发件人
    recipient_list = [email]  # 收件人
    # 正文 （带有html样式）
=======

from celery import Celery
from django.core.mail import send_mail
from django.conf import settings

# 创建celery应用对象
# 参数1： 一个自定义的名字
# 参数2： 使用Redis作为中间人
from django.template import loader

from apps.goods.models import GoodsCategory, IndexSlideGoods, IndexPromotion, IndexCategoryGoods

app = Celery('dailyfresh', broker='redis://127.0.0.1:6379/1')


@app.task
def send_active_email(username, receiver, token):
    """发送激活邮件"""
    subject = "天天生鲜用户激活"  # 标题, 不能为空，否则报错
    message = ""  # 邮件正文(纯文本)
    sender = settings.EMAIL_FROM  # 发件人
    receivers = [receiver]  # 接收人, 需要是列表
    # 邮件正文(带html样式)
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    html_message = ('<h3>尊敬的%s：感谢注册天天生鲜</h3>'
                    '请点击以下链接激活您的帐号:<br/>'
                    '<a href="http://127.0.0.1:8000/users/active/%s">'
                    'http://127.0.0.1:8000/users/active/%s</a>'
                    ) % (username, token, token)
<<<<<<< HEAD

    send_mail(subject, message, from_email, recipient_list,
=======
    send_mail(subject, message, sender, receivers,
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
              html_message=html_message)


@app.task
<<<<<<< HEAD
def generate_static_index_page():
    """生成静态首页"""
    sleep(2)
=======
def generate_static_index_html():
    """显示首页"""

>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    # 查询商品类别数据
    categories = GoodsCategory.objects.all()

    # 查询商品轮播轮数据
<<<<<<< HEAD
    # index为表示显示先后顺序的一个字段，值小的会在前面
=======
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    slide_skus = IndexSlideGoods.objects.all().order_by('index')

    # 查询商品促销活动数据
    promotions = IndexPromotion.objects.all().order_by('index')

    # 查询类别商品数据
    for category in categories:
        # 查询某一类别下的文字类别商品
        text_skus = IndexCategoryGoods.objects.filter(
            category=category, display_type=0).order_by('index')
        # 查询某一类别下的图片类别商品
<<<<<<< HEAD
        img_skus = IndexCategoryGoods.objects.filter(
            category=category, display_type=1).order_by('index')

        # 动态地给类别新增实例属性
        category.text_skus = text_skus
        # 动态地给类别新增实例属性
        category.img_skus = img_skus
=======
        image_skus = IndexCategoryGoods.objects.filter(
            category=category, display_type=1).order_by('index')
        # 动态地给类别新增实例属性
        category.text_skus = text_skus
        # 动态地给类别新增实例属性
        category.image_skus = image_skus

>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    # 定义模板数据
    context = {
        'categories': categories,
        'slide_skus': slide_skus,
        'promotions': promotions,
        'cart_count': 0,
    }
<<<<<<< HEAD
=======

    # 获取模板文件
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    template = loader.get_template('index.html')
    # 渲染生成标准备的html内容
    html_str = template.render(context)

<<<<<<< HEAD
    # # 生成一个叫index.html的文件: 放在桌面的static目录下
=======
    # 生成一个叫index.html的文件: 放在桌面的static目录下
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    file_path = '/home/python/Desktop/static/index.html'
    with open(file_path, 'w') as file:
        # 写入html内容
        file.write(html_str)
