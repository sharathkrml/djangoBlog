from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)           
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
  ##signal fired after object is saved
  ##we want a user profile created when an user is created
  #when a User is saved,send post_save signal and is receieved by receiever
    #receiever is create profile function    #instance of user
                     #if user is created         #**kwargs any excess keyword
                                #when a User is saved,send post_save signal and is receieved by receiever
                                        #receiever is create profile function    #instance of user
                                                         #if user is created