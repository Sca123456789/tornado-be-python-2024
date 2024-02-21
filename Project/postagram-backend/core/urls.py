from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from core.user.viewsets import UserViewSet

# Define router for DRF viewsets
router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    # Include admin URLs
    path('admin/', admin.site.urls),
    
    # Include DRF router URLs
    path('api/', include(router.urls)),
]
