from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from quiz.models import View,title_view,question_view

@login_required
def controller(request):
    sessions=Session.objects.filter(expire_date__gte=timezone.now())
    uids=[]
    for session in sessions:
        data=session.get_decoded()
        uids.append(data.get('_auth_user_id',None))
    active=User.objects.filter(id__in=uids)
    users=User.objects.all()
    home_views=View.objects.get(id=1)
    title_views=title_view.objects.get(id=1)
    question_views=question_view.objects.get(id=1)
    return render(request,'controller/main.html',{'active':active,'users':users,'home_views':home_views,'title_views':title_views,'question_views':question_views})
