import math
from django.shortcuts import redirect, render
from django.utils import timezone
from apps.user.models import User, Patient
from apps.lessons.models import Lesson, SetChoice, Subject
from apps.user.auth import access_auth
from apps.user.views import get_user_from_request
from django.http import JsonResponse
from django.conf import settings


@access_auth
def lessons_dashboard(request):
    
    user = get_user_from_request(request)
    patient = Patient.objects.get(adivisor=user)
    
    data = {
        'patient': patient,
        'programs': Lesson.objects.order_by('subject').distinct('subject').reverse()[:3]
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




@access_auth
def lessons_waiting_lesson(request):
    lesson = Lesson.objects.filter(is_active=True)
    data = {'is_next': False}
    if lesson.count() > 0:
        data['is_next'] = True
    
    return render(request, 'lessons/waiting-room.html', data)




@access_auth
def lessons_return_active(request):
    lesson = Lesson.objects.filter(is_active=True)
    data = { 'is_active': lesson.exists(), 'lesson': None, 'base_url': settings.BASE_URL }
    if lesson.exists():
        data['lesson'] = lesson[0].id

    return JsonResponse(data)





@access_auth
def lessons_play(request, slug):

    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson)
    current_choice = choice_control.last()

    data = {
        'base_url': settings.BASE_URL,
        'lesson': lesson,
        'options': lesson.boosts.split(';'),
        'choice_control': choice_control,
        'current_choice': current_choice,
        'coll_width': int(math.floor(12 / len(lesson.boosts.split(';')))) - 1,
    }

    return render(request, 'lessons/play-lesson.html', data)




@access_auth
def lessons_send_answer(request, slug):
    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson)
    current_choice = choice_control.last()

    current_choice.chosen_answer = request.GET['choice']
    current_choice.answer_date = timezone.now()
    current_choice.save()

    return redirect(f"{settings.BASE_URL}/lessons/{slug}/playlesson")





@access_auth
def lessons_game_admin(request, slug):
    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson)
    current_choice = choice_control.last()

    if not lesson.is_active:
        lesson.is_active = True
        lesson.save()

    if request.method == 'POST':
        current_choice.physical_help = request.POST['physical_help']
        current_choice.verbal_help = request.POST['verbal_help']
        current_choice.sequence_number = choice_control.count()
        current_choice.save()
        current_choice = SetChoice.objects.create(sequence_number=choice_control.count()+1, lesson=lesson, user=lesson.user)

    data = {
        'base_url': settings.BASE_URL,
        'lesson': lesson,
        'options': lesson.boosts.split(';'),
        'choice_control': choice_control,
        'current_choice': current_choice,
        'coll_width': int(math.floor(12 / len(lesson.boosts.split(';')))) - 1,
    }

    return render(request, 'lessons/admin-lesson.html', data)




@access_auth
def lessons_end_lesson(request, slug):
    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson)
    current_choice = choice_control.last()

    if request.method == 'GET':
        lesson.is_active = False
        lesson.save()
        if current_choice.chosen_answer is not None:
            current_choice.physical_help = request.GET['ph']
            current_choice.verbal_help = request.GET['vh']
            current_choice.sequence_number = choice_control.count()
            current_choice.save()
        else:
            SetChoice.objects.filter(id=current_choice.id).delete()

    return redirect(f"{settings.BASE_URL}/lessons")





@access_auth
def lessons_setchoice(request, slug):
    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson)

    if choice_control.count() == 0:
        setchoice = SetChoice()
        setchoice.lesson = lesson
        setchoice.user = lesson.user
        setchoice.sequence_number = choice_control.count()
        setchoice.correct_answer = request.GET['choice']
        setchoice.save()
    else:
        setchoice = choice_control.last()
        setchoice.correct_answer = request.GET['choice']
        setchoice.save()

    return redirect(f"{settings.BASE_URL}/lessons/{slug}/adminlessongame")





@access_auth
def lessons_is_next(request, slug):
    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson, chosen_answer__isnull=True, correct_answer__isnull=False)
    current_choice = choice_control.last()

    data = {'is_next': choice_control.count() > 0, 'has_active': lesson.is_active}

    if choice_control.count() > 0:
        data['correct_answer'] = current_choice.correct_answer
        data['current_choice'] = current_choice.id

    return JsonResponse(data)





@access_auth
def lessons_is_chosen(request, slug):
    lesson = Lesson.objects.get(id=slug)
    choice_control = SetChoice.objects.filter(lesson=lesson)
    current_choice = choice_control.last()
    return JsonResponse({
                            'is_chosen': current_choice.chosen_answer is not None,
                            'chosen_answer': current_choice.chosen_answer
                        })