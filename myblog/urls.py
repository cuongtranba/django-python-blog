from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.UserLogin,name='UserLogin'),
    url(r'^userlogout/$',views.UserLogout,name='UserLogout')
]
