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
        path('<slug:slug>/send_answer', views.lessons_send_answer, name='send_answer'),
        path('<slug:slug>/is_chosen', views.lessons_is_chosen, name='is_chosen'),
        path('<slug:slug>/is_next', views.lessons_is_next, name='is_next'),
        path('<slug:slug>/end_lesson', views.lessons_end_lesson, name='end_lesson'),
    ])),
]