from django.shortcuts import render
from apps.user.models import User, Patient
from apps.lessons.models import Lesson, Subject
from apps.user.auth import access_auth


@access_auth
def lessons_dashboard(request):
    
    user = User.objects.get(id=request.session['auth_session']['user'])
    patient = Patient.objects.get(adivisor=user)
    
    data = {
        'patient': patient,
        'programs': Lesson.objects.values('subject__subject', 'subject__description', 'subject__id').order_by('-id')[:3]
    }

    return render(request, 'lessons/lessons.html', data)


@access_auth
def lessons_add_subject(request):

    if request.method == 'POST':
        subject = Subject()
        subject.subject = request.POST['name']
        subject.description = request.POST['description']
        subject.user = User.objects.get(id=request.session['auth_session']['user'])
        subject.save()

    data = {
        'programs': Subject.objects.order_by('-id')[:6]
    }

    return render(request, 'lessons/add-subject.html', data)
