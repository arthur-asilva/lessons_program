from django.shortcuts import render

def lessons_dashboard(request):
    return render(request, 'lessons/lessons.html')
