from django.shortcuts import render

# Create your views here.
def video(request):
    return render(request,'videos/main.html')

def general_knowledge(request):
    return render(request,'videos/general_knowledge.html')

def general_science(request):
    return render(request,'videos/general_science.html')

def current_affairs(request):
    return render(request,'videos/current_affairs.html')

def government_exam(request):
    return render(request,'videos/government_exam.html')

def computer_science(request):
    return render(request,'videos/computer_science.html')