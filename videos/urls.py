from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.video,name="video"),
    url(r'^general_knowledge/$',views.general_knowledge,name="general_knowledge"),
    url(r'^general_science/$',views.general_science,name="general_science"),
    url(r'^current_affairs/$',views.current_affairs,name="current_affairs"),
    url(r'^government_exam/$',views.government_exam,name="government_exam"),
    url(r'^computer_science/$', views.computer_science, name="computer_science"),
]