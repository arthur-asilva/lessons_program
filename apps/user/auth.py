from django.shortcuts import redirect
from apps.user.models import User
from django.conf import settings

def access_auth(function):
    
    def decorator(request, *args, **kwargs):
        session = request.session.get('auth_session', None)
        
        if session is not None:
            if session['group'] == 1:
                # return redirect('http://localhost:8000/')
                pass
        else:
            return redirect(f"{settings.BASE_URL}/")

        return function(request, *args, **kwargs)

    return decorator