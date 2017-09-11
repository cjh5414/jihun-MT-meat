from django.conf.urls import url

from . import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^orderer$', views.input_order_info, name='input_order_info'),
]