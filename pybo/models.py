from django.db import models

# Create your models here.

class Question(models.Model) :
    subject = models.CharField(max_length=200)  #제목
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #질문과 같이 삭제된다.
    content = models.TextField()
    create_date = models.DateTimeField()
