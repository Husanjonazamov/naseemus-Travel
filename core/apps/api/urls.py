from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import TourView, BlogView

router = DefaultRouter()
router.register(r"tour", TourView, basename="tour")
router.register(r"blog", BlogView, basename="blog")


urlpatterns = [
    path("", include(router.urls)),
]
