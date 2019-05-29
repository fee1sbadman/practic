from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField(default='')
    bal = models.IntegerField(default = 0)


    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    right_choice = models.IntegerField(default = 1)


    def __str__(self):
        return self.name


class Choice(models.Model):
    question = models.ForeignKey(Question ,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)


    def __str__(self):
        return self.choice_text