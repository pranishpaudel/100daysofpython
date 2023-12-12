from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile,User

from django.apps import AppConfig
from django.core.signals import request_finished


@receiver(post_save, sender=Profile)
def update_user(sender,instance,created,**kwargs):
    profile= instance
    user= profile.user
    print(f"Signal: {user}")
    if created==False:
        user.first_name= profile.name
        user.username= profile.username
        user.email=profile.email
        user.save()




post_save.connect(update_user,sender=Profile)


