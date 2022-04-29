from django.shortcuts import render, redirect
from .models import User



def user_login(request):

    if request.method == 'POST':
        
        email, password = request.POST['email'], request.POST['password']
        user = User.objects.filter(email=email, password=password)
        
        if user.exists():
            user = user[0]
            request.session['auth_session'] = {'user': user.id, 'name': user.name, 'group': user.group}
            return user_redirect(user.group)


    return render(request, 'user/sign-in.html')




def user_redirect(group):
    
    if group != 1:
        return redirect('http://localhost:8000/lessons/')
    else:
        pass




def user_logout(request):
    del request.session['auth_session']
    return redirect('../')
