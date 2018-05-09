<<<<<<< HEAD
=======
from dailyfresh import settings
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
from django.contrib.auth.models import AbstractUser
from django.db import models
from itsdangerous import TimedJSONWebSignatureSerializer
from tinymce.models import HTMLField

<<<<<<< HEAD
from dailyfresh import settings
=======
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
from utils.models import BaseModel


class User(BaseModel, AbstractUser):
<<<<<<< HEAD
    """用户模型类"""

    def generate_active_token(self):
        """对字典数据{‘confirm’:10}加密，返回加密后的结果"""
        # 参数1：密钥
        # 参数２：有效时间　一天
        s = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 60 * 60 * 24)
        # self.id: 用户ｉｄ 类型为bytes
        datas = s.dumps({'confirm': self.id})  # type: bytes
        # bytes -> str
        return datas.decode()

    class Meta(object):
        # 指定表名 app01_user
        db_table = 'df_user'
=======
    class Meta:
        db_table = "df_user"

    def generate_active_token(self):
        """生成加密数据"""
        # 参数1：密钥，不能公开，用于解密
        # 参数２：加密数据失效时间(1天)
        serializer = TimedJSONWebSignatureSerializer(
            settings.SECRET_KEY, 3600 * 24)
        # 要加密的数据此处传入了一个字典，其格式是可以自定义的
        # 只要包含核心数据 用户id 就可以了，self.id即当前用户对象的id
        token = serializer.dumps({'confirm': self.id})
        # 类型转换： bytes -> str
        return token.decode()


class Test(models.Model):
    desc = HTMLField(verbose_name='商品描述', null=True)

    """测试"""
    ORDER_STATUS_CHOICES = (
        (1, "测试一"),
        (2, "测试二"),
        (3, "测试三"),
    )

    status = models.SmallIntegerField(default=1,
                                      verbose_name='订单状态',
                                      choices=ORDER_STATUS_CHOICES)

    class Meta(object):
        db_table = 'df_test'
        # 指定模型在后台显示的名称
        verbose_name = '测试模型'
        # 去除后台显示的名称默认添加的 's'
        verbose_name_plural = verbose_name
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e


class Address(BaseModel):
    """地址"""

    receiver_name = models.CharField(max_length=20, verbose_name="收件人")
    receiver_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    detail_addr = models.CharField(max_length=256, verbose_name="详细地址")
    zip_code = models.CharField(max_length=6, null=True, verbose_name="邮政编码")
    is_default = models.BooleanField(default=False, verbose_name='默认地址')

    user = models.ForeignKey(User, verbose_name="所属用户")

    class Meta:
        db_table = "df_address"
<<<<<<< HEAD


class TestModel(BaseModel):
    """测试用"""

    name = models.CharField(max_length=20)

    # 商品详情，使用第三方的: HTMLField
    goods_detail = HTMLField(default='', verbose_name='商品详情')





=======
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
