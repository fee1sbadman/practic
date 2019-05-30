from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    test = models.CharField(max_length=500)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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