

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login),  # 调用此子路由时会调用login方法
]