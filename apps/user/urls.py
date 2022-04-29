from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    # path('products/', include([
    #     path('add', views.Add, name='add'),
    #     path('<slug:slug>/get', views.Get, name='get'),
    #     path('<slug:slug>/delete', views.Delete, name='delete'),
    # ])),
]