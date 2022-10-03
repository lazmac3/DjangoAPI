from rest_framework import serializers
from .models import Status
from .models import Reaction
from django.contrib.auth.models import User
from .models import Like
from .models import DisLike


#These serializers determine the data that is available at the endpoints

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ('status','comment', 'reaction' )




class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('Title','status', 'author', 'Topic','Expiration_Time')
        

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','status','users')

  

class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = ('status','users')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class DataDumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id','Title','status','created_at', 'author', 'Topic','Expiration_Time','Poststatus','likes','dis_likes')
        depth=2

class ReactionSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ('comment', 'author_username', 'created_at')
        ordering = ['created_at']

class CommentsAndLikesSerializer(serializers.ModelSerializer):
    Poststatus = ReactionSerializerGet(many=True, read_only=True)
    
    class Meta:
        model = Status
        fields = ('id', 'Title','status','Topic','author_username','get_total_likes','get_total_dis_likes','overall_rating','created_at', 'Expiration_Time','Poststatus','update_expired','get_total_comments')
    
#https://stackoverflow.com/questions/22677070/additional-field-while-serializing-django-rest-framework tips on nesting    