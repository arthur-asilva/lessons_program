from tokenize import group
from django.shortcuts import render
from .models import User
from .auth import access_auth


@access_auth
def user_login(request):

    if request.method == 'POST':
        email, password = request.POST['email'], request.POST['password']
        user = User.objects.filter(email=email, password=password)
        if user.exists():
            user = user[0]
            request.session['auth_session'] = {'user': user.id, 'name': user.name, 'group': user.group}

    return render(request, 'sign-in.html')
