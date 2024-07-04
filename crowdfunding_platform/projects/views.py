from django.shortcuts import render

# Create your views here.
# projects/views.py
from rest_framework import viewsets # type: ignore
from .models import Project, Donation
from .serializers import ProjectSerializer, DonationSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
