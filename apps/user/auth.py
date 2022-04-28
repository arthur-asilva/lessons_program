def access_auth(function):
    
    def decorator(request, *args, **kwargs):
        session = request.session.get('auth_session', None)
        return function(request, *args, **kwargs)

    return decorator