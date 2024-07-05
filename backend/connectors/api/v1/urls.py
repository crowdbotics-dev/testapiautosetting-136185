from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136185ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136185", Testconnectors136185ViewSet, basename="testconnectors136185"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
