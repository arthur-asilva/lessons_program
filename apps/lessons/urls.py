from django.urls import path, include
from . import views

app_name = 'lessons'

urlpatterns = [
    path('lessons/', views.lessons_dashboard, name='home'),
    path('lessons/', include([
        path('add', views.lessons_add_subject, name='add'),
        path('<slug:slug>/addlesson', views.lessons_add_lesson, name='add_lesson'),
        path('<slug:slug>/adminlessongame', views.lessons_game_admin, name='admin_lesson_game'),
        path('<slug:slug>/playlesson', views.lessons_play, name='play_lesson_game'),
        path('<slug:slug>/setchoice', views.lessons_setchoice, name='setchoice'),
    ])),
]