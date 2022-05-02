from curses.ascii import US
from django.shortcuts import redirect, render
from apps.user.models import User, Patient
from apps.lessons.models import Lesson, Subject
from apps.user.auth import access_auth
from apps.user.views import get_user_from_request


@access_auth
def lessons_dashboard(request):
    
    user = get_user_from_request(request)
    patient = Patient.objects.get(adivisor=user)
    
    data = {
        'patient': patient,
        'programs': Lesson.objects.values('subject__subject', 'subject__description', 'subject__id', 'subject__creation_date').order_by('-id')[:3]
    }

    return render(request, 'lessons/lessons.html', data)





@access_auth
def lessons_add_subject(request):

    if request.method == 'POST':
        subject = Subject()
        subject.subject = request.POST['name']
        subject.description = request.POST['description']
        subject.user = get_user_from_request(request)
        subject.save()

    data = {
        'programs': Subject.objects.order_by('-id')[:6]
    }

    return render(request, 'lessons/add-subject.html', data)




@access_auth
def lessons_add_lesson(request, slug):

    subject = Subject.objects.get(id=slug)

    if request.method == 'POST':
        lesson = Lesson()
        lesson.user = User.objects.get(id=request.POST['patient'])
        lesson.boosts = ';'.join(request.POST.getlist('boost'))
        lesson.subject = subject
        lesson.lesson_date = request.POST['lesson_date']
        lesson.description = request.POST['description']
        lesson.save()
        return redirect('../../lessons')

    data = {
        'lessons': Lesson.objects.filter(subject__id=slug).order_by('-id'),
        'subject': subject,
        'users': User.objects.filter(group=1)
    }

    return render(request, 'lessons/add-lesson.html', data)
