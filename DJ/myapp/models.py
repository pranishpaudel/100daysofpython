from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner= models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    title= models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    featured_img= models.ImageField(blank=True,null=True,default="default.svg")
    demo_link= models.CharField(max_length=2000)
    source_link= models.CharField(max_length=2000,null=True,blank=True)
    tags= models.ManyToManyField('Tag',blank=True)
    vote_total= models.IntegerField(default=0,null=True,blank=True)
    vote_ratio= models.IntegerField(default=0,null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4
                         ,unique=True,
                         primary_key=True
                         ,editable=False)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ['-vote_ratio','-vote_total']
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        # Avoid division by zero
        ratio = (upVotes / totalVotes) * 100 if totalVotes != 0 else 0

        self.vote_total = totalVotes
        self.vote_ratio = int(ratio)
        self.save()
    

class Review(models.Model):


    VOTE_TYPE= (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )

    owner= models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body= models.TextField(null=True,blank=True)
    value= models.CharField(max_length=200,choices=VOTE_TYPE)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    class Meta:
        unique_together= [['owner','project']]


    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)   


    def __str__(self):
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    recepient= models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,related_name="messages")
    name= models.CharField(max_length=200,null=True,blank=True)
    email= models.CharField(max_length=200,null=True,blank=True)
    subject= models.CharField(max_length=200,null=True,blank=True)
    body= models.TextField(max_length=1000,null=True,blank=True)
    is_read= models.BooleanField(default=False,null=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 

    def __str__(self):
        return self.subject
    class Meta:
        ordering= ['is_read','-created']
    


    





