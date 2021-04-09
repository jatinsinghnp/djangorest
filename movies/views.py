from django.shortcuts import render
from .serilizers import MovieSerilizer
from rest_framework import viewsets
from .models import MovieData
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset=MovieData.objects.all()
    serializer_class=MovieSerilizer


class ActionViewset(viewsets.ModelViewSet):
    queryset=MovieData.objects.filter(typ="action")
    serializer_class=MovieSerilizer
class ComedyViewset(viewsets.ModelViewSet):
    queryset=MovieData.objects.filter(typ="comedy")
    serializer_class=MovieSerilizer