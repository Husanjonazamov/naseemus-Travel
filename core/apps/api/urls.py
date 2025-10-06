from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import TourView, BlogView, HolidaysView, BanerView, OrderView, HotelView

router = DefaultRouter()
router.register(r"tour", TourView, basename="tour")
router.register(r"blog", BlogView, basename="blog")
router.register(r"holidays", HolidaysView, basename="holidays")
router.register(r"banner", BanerView, basename="banner")
router.register(r"order", OrderView, basename="order")
router.register(r"hotel", HotelView, basename="hotel")



urlpatterns = [
    path("", include(router.urls)),
]
