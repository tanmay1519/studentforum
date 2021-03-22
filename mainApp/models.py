from django.db import models

# Create your models here.
class user (models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    branch=models.CharField(max_length=10)

class question(models.Model):
    question_id=models.AutoField(primary_key=True)
    user_id=models.CharField(max_length=100)
    question=models.CharField(max_length=200)
    topic=models.CharField(max_length=50)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
class answer(models.Model):
    user_id=models.CharField(max_length=100)
    question_id=models.CharField(max_length=100)
    answer_id=models.AutoField(primary_key=True)
    answer=models.CharField(max_length=1000)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
