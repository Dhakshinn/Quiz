from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^email/',views.email_to_all,name="message"),
    url(r'^Signup/$',views.signup,name="signup"),
    url(r'^profile/$',views.profile,name="profile"),
    url(r'^contest/$',views.contest,name="contest"),
    url(r'^create_quiz/$', views.quiz_create, name="create_quiz"),
    url(r'^signup_contest/(?P<title>.+)/$',views.signup_contest,name="signup_contest"),
    url(r'^quiz_question/(?P<title>.+)/$',views.quiz_ques,name="create_quiz_question"),
    url(r'^List_question/(?P<title>.+)/$',views.List_question,name="List_contest_question"),
    url(r'^edit_question/(?P<pk>[0-9]+)/$',views.UpdateQuestion.as_view(),name="edit_quiz_question"),
    url(r'^contest_scoreboard/(?P<title>.+)/$',views.scoreboard_contest,name="contest_score"),
    url(r'^contest_evaluation/(?P<title>.+)/(?P<pk>[0-9]+)/$',views.contest_evaluation,name="contest_evaluation"),
    url(r'^list/(?P<track>.+)/(?P<title>.+)/$',views.list_content,name="List"),
    url(r'^question/(?P<track>.+)/(?P<title>.+)/(?P<topic>.+)/(?P<pk>[0-9]+)/$', views.list_questions, name="question"),
    url(r'^scoreboard_main/(?P<title>.+)/(?P<track>.+)/$',views.scoreboard_main,name="main_score"),
]
