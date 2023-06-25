from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudyGroup


# class GroupsAPIView(ListAPIView):
#     queryset = StudyGroup.objects.all()

class GroupsAPIView(APIView):
    def get(self, request):
        queryset = StudyGroup.objects.all().values()
        return Response({'groups':list(queryset)})