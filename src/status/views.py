from django.shortcuts import render
#https://medium.com/@sarit.r/djangofilterbackend-searchfilter-orderingfilter-example-dbe8e56ff1fc for filtering
# Create your views here.
from rest_framework import viewsets
from .models import Status
from .models import Reaction
from .models import Like
from .models import DisLike
from django.contrib.auth.models import User
from .serializers import StatusSerializer
from .serializers import ReactionSerializer
from .serializers import UserSerializer
from .serializers import LikeSerializer
from .serializers import DisLikeSerializer
from .serializers import DataDumpSerializer
from .serializers import CommentsAndLikesSerializer
from rest_framework import filters
from datetime import timedelta
from datetime import datetime
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

        
#These view determine what appears at the endpoints, who can view them (basically only admin) and how the methods can be ordered and searched by GET requests
class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['Topic', 'id']

    

class ReactionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']

    

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']

class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status']






    

class DisLikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status']

class DataDumpViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = DataDumpSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']

class StatusCommentsAndLikesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = CommentsAndLikesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id','Topic']
    http_method_names = ['get', 'head']



#this is the test webpage copied from the notes
def myapp_hi(request): #server takes a request used a test in this app too will leave in
    return render(request,'helloworld.html',{})

# ADD THE FOLLOWING TO RETURN ALL THE OBJECTS (DATA) This is an expanded version of the lab code for my small front end site
def piazza_status(request):
    status_list = Status.objects.all().order_by('-updated_at') # SELECT ALL!
    reaction_list=Reaction.objects.all()
    user_list=User.objects.all()
    like_list=Like.objects.all()
    dis_like_list=DisLike.objects.all()
    return render(request,'view_status.html',{'statuses':status_list, 'reactions':reaction_list, 'users':user_list,'likes':like_list,'dislikes': dis_like_list})

