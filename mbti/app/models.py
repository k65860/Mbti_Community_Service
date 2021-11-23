from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

class Write(models.Model):
    title = models.CharField(max_length=200) #제목
    people = models.CharField(null=True,default='',max_length=50) #작성자
    contents = models.TextField() #내용
    updated_at = models.DateTimeField(auto_now=True) #업로드시각