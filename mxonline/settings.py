"""
Django settings for mxonline project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# *******指定生成的startapp到apps目录*********
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(2g%(n-%7o7i)5zr4igkayy+h31#2y0@xlq%3yz&=cn9$b#6lx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# #自定义验证 用邮箱登录
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'operation',
    'organization',
    'xadmin', #后台
    'crispy_forms', #验证码
    'captcha', #验证码
    'pure_pagination', #分页
]

#在通过AbstractUser类创建用户类时，可添加自定义字段，同时必须注意的是继承该类必须在setting.py中声明使用，
# 一旦指定了新的认证系统使用的表，必须重新在数据库中创建该表，不能使用原来的auth_user表
AUTH_USER_MODEL = "users.Userprofile"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mxonline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',#配置展示的上传文件目录MEDIA_URL才能生效
            ],
            'builtins' : [ #静态文件夹目录
                'django.templatetags.static'
            ],
        },
    },
]

WSGI_APPLICATION = 'mxonline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'mxonline',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1'

    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#切换到中文
LANGUAGE_CODE = 'zh-hans'

#时区改到上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#改为本地实际 True是国际时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#设置静态文件目录

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

#上传文件路径配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')




#自动发送邮件配置
EMAIL_USE_SSL = True
EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 465
EMAIL_HOST_USER ="515749390@qq.com"
EMAIL_HOST_PASSWORD = "gkecqtndfbhqbhfj"
EMAIL_FROM = "515749390@qq.com"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#分页设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}