from django.shortcuts import render
from apps.user.models import User, Patient

def lessons_dashboard(request):
    print(request.session['auth_session'])
    # patients = Patient.objects.get(advisor)
    return render(request, 'lessons/lessons.html')
