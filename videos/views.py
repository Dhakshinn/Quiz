from django.shortcuts import render
from .models import computer_science_view,current_affairs_view,general_knowledge_view,general_science_view,government_exam_view

# Create your views here.
def video(request):
    return render(request,'videos/main.html')

def general_knowledge(request):
    if request.user.username == 'dhakshin':
        pass
    else:
        a=general_knowledge_view.objects.get(id=1)
        a.view = a.view + 1
        a.save()
    return render(request,'videos/general_knowledge.html')

def general_science(request):
    if request.user.username == 'dhakshin':
        pass
    else:
        a = general_science_view.objects.get(id=1)
        a.view = a.view + 1
        a.save()
    return render(request,'videos/general_science.html')

def current_affairs(request):
    if request.user.username == 'dhakshin':
        pass
    else:
        a = current_affairs_view.objects.get(id=1)
        a.view = a.view + 1
        a.save()
    return render(request,'videos/current_affairs.html')

def government_exam(request):
    if request.user.username == 'dhakshin':
        pass
    else:
        a = government_exam_view.objects.get(id=1)
        a.view = a.view + 1
        a.save()
    return render(request,'videos/government_exam.html')

def computer_science(request):
    if request.user.username == 'dhakshin':
        pass
    else:
        a = computer_science_view.objects.get(id=1)
        a.view = a.view + 1
        a.save()
    return render(request,'videos/computer_science.html')