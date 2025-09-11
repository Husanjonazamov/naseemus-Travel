from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import TourView, BlogView, HolidaysView, BanerView

router = DefaultRouter()
router.register(r"tour", TourView, basename="tour")
router.register(r"blog", BlogView, basename="blog")
router.register(r"holidays", HolidaysView, basename="holidays")
router.register(r"banner", BanerView, basename="banner")




urlpatterns = [
    path("", include(router.urls)),
]
