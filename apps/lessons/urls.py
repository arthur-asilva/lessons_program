from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('lessons/', views.lessons_dashboard, name='lessons_dashboard'),
    # path('products/', include([
    #     path('add', views.Add, name='add'),
    #     path('<slug:slug>/get', views.Get, name='get'),
    #     path('<slug:slug>/delete', views.Delete, name='delete'),
    # ])),
]