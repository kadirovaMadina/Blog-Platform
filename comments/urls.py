from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet


router = routers.DefaultRouter()
router.register("comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
