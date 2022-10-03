from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import timedelta
from datetime import datetime
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Q





# Create your models here 
#https://stackoverflow.com/questions/8016412/in-django-do-models-have-a-default-timestamp-field timestamp code
#https://stackoverflow.com/questions/34305805/django-foreignkeyuser-in-models
#https://stackoverflow.com/questions/39883950/str-returned-non-string-type-tuple used to remove tuple error
#https://docs.djangoproject.com/en/3.1/ref/models/fields/ choicefield
#https://medium.com/djangotube/django-like-and-dislike-buttons-model-design-like-youtube-f152b95e7f21 for likes and dislikes
#https://stackoverflow.com/questions/15307623/cant-compare-naive-and-aware-datetime-now-challenge-datetime-end timezone

#main mode
class Status(models.Model):
    Title = status = models.CharField(max_length=100, default='title')
    status = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name = 'status_author', default=9999, null=False)
    Topic_Choices = (
        ('Politics', 'Politics'),
        ('Health', 'Health'),
        ('Sport', 'Sport'),
        ('Tech', 'Tech'),
    )
    Topic = models.CharField(max_length=8, choices=Topic_Choices, default = 'Politics')
    Expiration_Time = models.DurationField(default=timedelta(minutes=5),)
    
    #These poperties are calculated fields that are needed for the GET requests
    @property
    def get_total_likes(self):
        return self.likes.count()

    @property
    def get_total_dis_likes(self):
        return self.dis_likes.count()
    
    #doesnt work
    @property
    def overall_rating(self):
        return self.likes.count()-self.dis_likes.count()
  

    @property
    def get_total_comments(self):
        return self.Poststatus.count()
    
    @property
    def author_username(self):
        return self.author.username

    #debugging time zone function ouput on view, but can use correctly with validation rules
    @property
    def update_expired(self):
        now = timezone.now()
        return (now >= (self.created_at + self.Expiration_Time))
 

    def __str__(self): 
        return '%s %s %s '%(self.status, self.author, self.updated_at)
    class Meta:
        ordering = ['updated_at']

#This is to allow people to comment on status       
    
class Reaction(models.Model):
    status=models.ForeignKey(Status, on_delete=models.CASCADE, blank=True ,related_name='Poststatus')
    comment=models.CharField(max_length=200,blank=True)
    reaction = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'requirement_comment', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def author_username(self):
        return self.reaction.username

    def __str__(self): 
        return '%s %s'%(self.reaction, self.created_at)

#This prevents a reaction being saved if the post is expired
    def save(self, *args, **kwargs):
        now = timezone.now()   
        if(now >= (self.status.created_at + self.status.Expiration_Time)):
            raise ValidationError('Expired Post, you can watch but not interact')
        super().save(*args, **kwargs) 

#This is for liking status
class Like(models.Model):
    status = models.ForeignKey(Status, related_name="likes", on_delete=models.CASCADE)
    users = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status.status)[:30]

#This prevents a person liking their own status, liking more than once to liking an expired status
    def save(self, *args, **kwargs):
        now = timezone.now()   
        Like_data = Like.objects.all()
        if(now >= (self.status.created_at + self.status.Expiration_Time)):
            raise ValidationError('Expired Post, you can watch but not interact')
        elif(int(self.status.author.id)==int(self.users.id)):
                raise ValidationError('Your Post, You can not like it')
        else:
            for element in Like_data:
                if(int(self.users.id) == int(element.users.id) and (int(self.status.id) == int(element.status.id))):
                    raise ValidationError('already liked')
        super().save(*args, **kwargs)    

#This is to dislike and is a mirror of the like status
class DisLike(models.Model):
    status = models.ForeignKey(Status, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='requirement_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status.status)[:30]  

    def save(self, *args, **kwargs):
        now = timezone.now()   
        Dis_Like_data = Like.objects.all()
        if(now >= (self.status.created_at + self.status.Expiration_Time)):
            raise ValidationError('Expired Post, you can watch but not interact')
        elif(int(self.status.author.id)==int(self.users.id)):
                raise ValidationError('Your Post, You can not like it')
        else:
            for element in Dis_Like_data:
                if(int(self.users.id) == int(element.users.id) and (int(self.status.id) == int(element.status.id))):
                    raise ValidationError('already liked')
        super().save(*args, **kwargs)   

