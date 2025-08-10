from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryView,
    ListingView,
    PostingView,
    FeatureView
)

router = DefaultRouter()

router.register(r"category", CategoryView, basename="category")
router.register(r"listing", ListingView, basename="listing")
router.register(r"posting", PostingView, basename="posting")
router.register(r"feature", FeatureView, basename="feature")



urlpatterns = [
    path("", include(router.urls)),
]
