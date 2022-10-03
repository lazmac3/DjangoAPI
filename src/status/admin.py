from django.contrib import admin
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Register your models here.
from .models import Status # Import Characters class as model
admin.site.register(Status) # Register the Character class in
from .models import Reaction
admin.site.register(Reaction)

from .models import Like
admin.site.register(Like)

from .models import DisLike
admin.site.register(DisLike)



