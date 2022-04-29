from django.urls import path, include
from . import views

app_name = 'lessons'

urlpatterns = [
    path('lessons/', views.lessons_dashboard, name='home'),
    path('lessons/', include([
        path('add', views.lessons_add_subject, name='add'),
        # path('<slug:slug>/get', views.Get, name='get'),
        # path('<slug:slug>/delete', views.Delete, name='delete'),
    ])),
]