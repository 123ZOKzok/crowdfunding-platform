# projects/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, DonationViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add other URLs as needed
]
