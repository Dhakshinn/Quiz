from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm,Create_Quiz_Form,Create_Quiz_Question
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate,login
from .models import track_details,title_details,topic_details,View,create_quiz,questions,user_solved,programming_score,title_view,\
    question_view,contest_scores,quiz_questions,scoreboard_track
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

# ----------------------------------------DASHBOARD-------------------------------------------------------------------------------
def home(request):
    a = track_details.objects.all()
    x=View.objects.get(id=1)
    x.views = x.views +1
    x.save()
    return render(request,'quiz/Base.html',context={'a':a})


@login_required
def list_content(request,track,title):
    a=title_view.objects.get(id=1)
    a.views=a.views+1
    a.save()
    a=title_details.objects.all()
    if scoreboard_track.objects.filter(user_name=request.user.username,track=track).exists():
        s = scoreboard_track.objects.get(user_name=request.user.username,track=track)
    else:
        s = scoreboard_track()
        s.user_name = request.user.username
        s.track=track
        s.save()
        s = scoreboard_track.objects.get(user_name=request.user.username,track=track)
    return render(request, 'quiz/title_details.html', context={'a': a,'title':title,'track':track,'scoreboard':s})

def list_questions(request,track,title,topic):
    a=question_view.objects.get(id=1)
    a.views=a.views+1
    a.save()
    a=topic_details.objects.all()
    solved = user_solved.objects.get(name=request.user.username)
    s = scoreboard_track.objects.get(user_name=request.user.username, track=track)
    return render(request,'quiz/questions.html',context={'a':a,'title':title,'track':track,'topic':topic,'solved':solved,'scoreboard':s})

def evaluation(request,track,title,topic,pk):
    a = topic_details.objects.all()
    x=questions.objects.get(id=pk)
    solved=user_solved.objects.get(name=request.user.username)
    if request.method == "POST":
        data=[]
        for key in request.POST:
            data.append(request.POST[key])
        if request.POST[key]==x.answer:
            if request.user.is_authenticated():
                username=request.user.username
                user=user_solved.objects.get(name=username)
                user.questions_solved.add(x)
                user.save()
                s = scoreboard_track.objects.get(user_name=username,track=track)
                s.score = s.score + 10
                s.save()
        else:
            username = request.user.username
            user = user_solved.objects.get(name=username)
            user.questions_solved.add(x)
            user.save()
            s = scoreboard_track.objects.get(user_name=request.user.username,track=track)
    return render(request,'quiz/questions.html',context={'a':a,'title':title,'track':track,'topic':topic,'solved':solved,'scoreboard':s})

def scoreboard_main(request,title,track):
    score=scoreboard_track.objects.filter(track=track).order_by('-score')
    return render(request,'quiz/main_scoreboard.html',{'contest_score':score,'track':track})

#--------------------------CONTEST--------------------------------------------------------------------------------------------

@login_required
def contest(request):
    quizes=create_quiz.objects.all()
    return render(request,'quiz/contest.html',{'quizes':quizes})

def signup_contest(request,title):
    if contest_scores.objects.filter(name=request.user.username,title=title).exists():
        pass
    else:
        a = contest_scores()
        a.title = title
        a.name = request.user.username
        a.save()
    quiz=create_quiz.objects.get(title=title)
    contest_score = contest_scores.objects.get(name=request.user.username, title=title)
    return render(request,'quiz/contest_question.html',{'quiz':quiz,'contest_score':contest_score})


def contest_evaluation(request,title,pk):
    ques=quiz_questions.objects.get(id=pk)
    if request.method == 'POST':
        contest_score=contest_scores.objects.get(name=request.user.username,title=title)
        contest_score.quiz_questions.add(ques)
        data = []
        for key in request.POST:
            data.append(request.POST[key])
        if request.POST[key] == ques.answer:
            contest_score.score = contest_score.score +1
            contest_score.save()
    quiz = create_quiz.objects.get(title=title)
    contest_score = contest_scores.objects.get(name=request.user.username, title=title)
    return render(request, 'quiz/contest_question.html', {'quiz': quiz,'contest_score':contest_score})

def scoreboard_contest(request,title):
    contest_score=contest_scores.objects.filter(title=title).order_by('-score')
    return render(request,'quiz/contest_scoreboard.html',{'contest_score':contest_score,'title':title})
#----------------------------------------CREATE QUIZ----------------------------------------------------------------------------

@login_required
def quiz_create(request):
    if request.method=="GET":
        form=Create_Quiz_Form()
    else:
        form=Create_Quiz_Form(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                form.instance.name=request.user.username
                form.save()
            return redirect('profile')
    return render(request,'quiz/create_quiz1.html',{'form':form})


def quiz_ques(request,title):
    form=Create_Quiz_Question()
    if request.method=="POST":
        form=Create_Quiz_Question(request.POST)
        if form.is_valid():
            instance=form.save()
            user=create_quiz.objects.get(title=title)
            user.questions.add(instance)
            user.save()
        return redirect('profile')
    return render(request,'quiz/create_question.html',{'form':form})

def List_question(request,title):
    questions=create_quiz.objects.get(title=title)
    return render(request,'quiz/List_contest_question.html',{'a':questions})


class UpdateQuestion(UpdateView):
    model = quiz_questions
    template_name = 'quiz/update_question.html'
    fields = '__all__'
    success_url = reverse_lazy('profile')


#-------------------------------------------------AUTHENTICATION------------------------------------------------------

def signup(request):
    if request.method=='GET':
        form=UserForm()
    else:
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            address=form.cleaned_data.get('email')
            email = EmailMessage('HACKERQUIZ', 'Hi ,thank you for signing up HACKERQUIZ....', to=[address])
            #email.send()
            username = form.cleaned_data.get('username')
            raw_pass= form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_pass)
            login(request,user)
            solved=user_solved()
            solved.name=request.user.username
            solved.save()
            return redirect('home')
    return render(request,'registration/signup.html',{'form':form})

@login_required
def email_to_all(request):
    if request.user.username == 'dhakshin':
        users = User.objects.all()
        for x in users:
            address = x.email
            user_name = x.username
            msg = 'Hello ' + str(user_name) + ',\n\t' + 'There is a new track available to brush your skills.....'  + '\n\n\n\n' + 'Have a good Day!' + '\n\n' + 'The HackerQuiz Team'
            email = EmailMessage('HACKERQUIZ', msg, to=[address])
            email.send()
        return redirect('home')
    else:
        return redirect('home')



def profile(request):
    a = create_quiz.objects.filter(name=request.user.username)
    scores=scoreboard_track.objects.filter(user_name=request.user.username)
    return render(request,'quiz/profile.html',{'a':a,'scores':scores})
