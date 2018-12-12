from django.db import models
from django.contrib.auth.models import User

#--------------------------------------DASHBOARD---------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
class title(models.Model):
    title_name=models.CharField(max_length=100)
    def clean(self):
        self.title_name=self.title_name.upper()
    def __str__(self):
        return self.title_name

class track_details(models.Model):
    track_name=models.CharField(max_length=100)
    titles=models.ManyToManyField('title')

    def __str__(self):
        return self.track_name
    def clean(self):
        self.track_name=self.track_name.upper()

class topic(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def clean(self):
        self.name=self.name.upper()


class questions(models.Model):
    ques=models.TextField(max_length=1000)
    option1=models.CharField(max_length=100,null=True)
    option2=models.CharField(max_length=100,null=True)
    option3=models.CharField(max_length=100,null=True)
    option4=models.CharField(max_length=100,null=True)
    answer=models.CharField(max_length=100,default="ans")

    def __str__(self):
        return self.ques

class title_details(models.Model):
    title_name=models.ForeignKey(title)
    topics=models.ManyToManyField('topic')

    def __str__(self):
        return self.title_name.title_name

class topic_details(models.Model):
    topic_name=models.ForeignKey(topic)
    questions=models.ManyToManyField('questions')

    def __str__(self):
        return self.topic_name.name


class scoreboard_track(models.Model):
    track=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    score=models.IntegerField(default=0)

#------------------------------------------------USER MODELS-----------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

class user_solved(models.Model):
    name=models.CharField(max_length=100)
    questions_solved=models.ManyToManyField("questions",blank=True)

    def __str__(self):
        return self.name


class View(models.Model):
    views=models.IntegerField()

class title_view(models.Model):
    views=models.IntegerField()

class question_view(models.Model):
    views=models.IntegerField()


#-----------------------------------------------------CREATE QUIZ MODELS----------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------


class quiz_questions(models.Model):
    question=models.TextField(max_length=200)
    option1=models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class create_quiz(models.Model):
    name=models.CharField(max_length=100,blank=True)
    title=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    questions=models.ManyToManyField('quiz_questions',blank=True)

    def __str__(self):
        return '%s-%s' %(self.name,self.title)

class contest_scores(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    score=models.IntegerField(default=0)
    quiz_questions=models.ManyToManyField('quiz_questions',blank=True)
