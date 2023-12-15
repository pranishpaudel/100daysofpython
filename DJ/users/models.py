from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import uuid
import smtplib


  

# Create your models here.
class Profile(models.Model):

    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200,blank=True,null=True)
    username= models.CharField(max_length=200,blank=True,null=True)
    location= models.CharField(max_length=200,blank=True,null=True)
    email= models.EmailField(max_length=500,blank=True,null=True)
    short_intro= models.CharField(max_length=200,blank=True,null=True)
    bio= models.TextField(blank=True,null=True)
    profile_image= models.ImageField(null=True,blank=True,upload_to='profiles/',default="profiles/user-default.png")
    social_github= models.CharField(max_length=200,blank=True,null=True)
    social_linkedin= models.CharField(max_length=200,blank=True,null=True)
    social_youtube= models.CharField(max_length=200,blank=True,null=True)
    social_website= models.CharField(max_length=200,blank=True,null=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)
    



class Skill(models.Model):

    owner= models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200,blank=True,null=True)
    description_for_skill= models.TextField(blank=True,null=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)   

    def __str__(self):
        return str(self.name)

# @receiver(post_save,sender=Profile)
def CreateUser(sender,instance,created,**kwargs):
    if created:
        user= instance
        profile= Profile.objects.create(
             user= user,
             username= user.username,
             email= user.email,
             name= user.first_name,
         )
                 
        my_email= "pkpoudelpranishma@gmail.com"
        password= "jfew wwbj szja ijki"
        connection= smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr= my_email
                                    , to_addrs= profile.email,
                                    msg=f"Subject:Welcome Email \n We're glad to be welcome you here")
        connection.close()

def deleteUser(sender,instance,**kwargs):
    print("deleting user...")
    
post_save.connect(CreateUser,sender=User)

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


# post_delete.connect(deleteUser,sender=Profile)