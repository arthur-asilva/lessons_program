from django.shortcuts import render, redirect
from .models import User
from apps.lessons.models import Lesson
from django.conf import settings



def user_login(request):

    if request.method == 'POST':
        
        email, password = request.POST['email'], request.POST['password']
        user = User.objects.filter(email=email, password=password)
        
        if user.exists():
            user = user[0]
            request.session['auth_session'] = {'user': user.id, 'name': user.name, 'group': user.group}
            active_lesson = Lesson.objects.filter(is_active=True, user=user)
            return user_redirect(user.group, active_lesson)

    return render(request, 'user/sign-in.html')



def user_redirect(group, active=0):
    
    if group != 1:
        return redirect(f"{settings.BASE_URL}/lessons/")
    else:
        if active.count() > 0:
            return redirect(f"{settings.BASE_URL}/lessons/{active[0].id}/playlesson")
        else:
            return redirect(f"{settings.BASE_URL}/lessons/waiting_room")
            





def user_logout(request):
    del request.session['auth_session']
    return redirect('../')



def get_user_from_request(request):
    user = User.objects.get(id=request.session['auth_session']['user'])
    return user