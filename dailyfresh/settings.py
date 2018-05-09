"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

<<<<<<< HEAD
from django.conf.global_settings import AUTH_USER_MODEL
=======
from django.conf.global_settings import STATICFILES_DIRS
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = '-7m$aw5&@aki01t3v-j^g&vi8gt3bu(*(z+(hul3wbs#w1$!h7'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = []
DEBUG = 'False'
ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',  # 使用Django自带的用户认证模块
=======
SECRET_KEY = '*ts8w^(p!34&!wctdmxb!k63zx2+%!-!kzf78a3(c!bh)ncqa_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',  # 后台管理模块
    'django.contrib.auth',  # Django自带用户认证模块
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'apps.cart',  # 购物车模块
    'apps.goods',  # 商品模块
    'apps.orders',  # 订单模块
    'apps.users',  # 用户模块
    'tinymce',  # 使用应用
    # 使用haystack全文检索框架
    'haystack',

)
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',  # 丰富样式
    'width': 600,
    'height': 400,
}
=======
    'apps.users',  # 用户模块
    'apps.orders',  # 订单模块
    'apps.goods',  # 商品模块
    'apps.cart',  # 购物车模块
    "tinymce",  # 富文本控件
)

>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dailyfresh.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 配置mysql数据库
=======
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "db_dailyfresh",
        'USER': "root",
        'PASSWORD': "mysql",
        'HOST': "localhost",
<<<<<<< HEAD
        'PORT': 3306,
=======
        'PORT': "3306",
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

<<<<<<< HEAD
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
AUTH_USER_MODEL = 'users.User'

# # 邮件发送配置
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 导入邮件模块
# EMAIL_HOST = 'smtp.qq.com'  # 邮箱服务器地址
# EMAIL_PORT = 465  # 邮箱服务器端口（默认都为25）
# EMAIL_HOST_USER = 'ruguo@qq.com'  # 发件人（天天生鲜官方邮箱账号）
# EMAIL_HOST_PASSWORD = 'svlpfegpiwytbiee'  # 客户端授权码，非邮箱登录密码
# EMAIL_FROM = '天天生鲜<ruguo@qq.com>'  # 打开邮件显示在‘发件人’中的签名
=======
DEFAULT_FILE_STORAGE = 'utils.fastdfs.storage.FdfsStorage'

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

AUTH_USER_MODEL = "users.User"

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',  # 丰富样式
    'width': 600,
    'height': 400,
}
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e

# 邮件发送配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 导入邮件模块
EMAIL_HOST = 'smtp.163.com'  # 邮箱服务器地址
EMAIL_PORT = 25  # 邮箱服务器端口（默认都为25）
EMAIL_HOST_USER = 'luje128@163.com'  # 发件人（天天生鲜官方邮箱账号）
EMAIL_HOST_PASSWORD = 'cjb930926'  # 客户端授权码，非邮箱登录密码
EMAIL_FROM = '天天生鲜<luje128@163.com>'  # 打开邮件显示在‘发件人’中的签名

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        "LOCATION": "redis://127.0.0.1:6379/2",
=======
        "LOCATION": "redis://127.0.0.1:6379/1",
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": ""
        }
    }
}
<<<<<<< HEAD

# session数据缓存到Redis中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FdfsStorage'

# 配置haystack框架
HAYSTACK_CONNECTIONS = {
    'default': {
        # # 使用whoosh搜索引擎
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 使用whoosh搜索引擎(使用jiebar中文分词工具)
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 指定生成的索引库保存在哪个目录下
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 当添加、修改、删除了数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
# 指定收集的静态文件保存在哪个目录下：
STATIC_ROOT = '/home/python/Desktop/static'
=======
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
LOGIN_URL = '/users/login'
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
